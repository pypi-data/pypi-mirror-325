import json
import math
import re
import threading
import time
from dataclasses import dataclass
from typing import Any, Awaitable, Callable, Dict, Generic, List, Optional, Union, final

from ..apis import MaximAPI
from ..models import (
    DatasetRow,
    DataStructure,
    DataValue,
    Evaluator,
    EvaluatorType,
    HumanEvaluationConfig,
    PlatformEvaluatorType,
    RunResult,
    RunStatus,
    RunType,
    T,
    TestRun,
    TestRunConfig,
    TestRunEntry,
    TestRunLogger,
    TestRunStatus,
    TestRunWithDatasetEntry,
    YieldedOutput,
    YieldedOutputMeta,
)
from ..utils import Semaphore


def calculate_polling_interval(
    timeout_minutes: float, is_ai_evaluator_in_use: bool = False
) -> int:
    points = [
        (10, 5),
        (15, 5),
        (30, 10),
        (60, 15),
        (120, 30),
        (1440, 120),
    ]

    lower_point = points[0]
    upper_point = points[-1]
    for i in range(len(points) - 1):
        if points[i][0] <= timeout_minutes <= points[i + 1][0]:
            lower_point = points[i]
            upper_point = points[i + 1]
            break

    x1, y1 = lower_point
    x2, y2 = upper_point
    if x1 == x2:
        return y1

    t = (timeout_minutes - x1) / (x2 - x1)
    p = 2
    interpolated_value = y1 + (y2 - y1) * pow(t, p)

    return min(max(round(interpolated_value), 15 if is_ai_evaluator_in_use else 5), 120)


def get_all_keys_by_value(obj: Optional[dict[Any, Any]], value: Any) -> List[str]:
    if obj is None:
        return []
    return [key for key, val in obj.items() if val == value]


def get_sliced_value(value: Any) -> str:
    if isinstance(value, str):
        return value[:20] + "..." if len(value) > 20 else value
    else:
        stringified_value = json.dumps(value)
        return (
            stringified_value[:20] + "..."
            if len(stringified_value) > 20
            else stringified_value
        )


def sanitize_evaluators(
    platform_evaluators: Optional[list[PlatformEvaluatorType[T]]],
) -> None:
    """
    Sanitize the list of platform evaluators to ensure unique names.

    Args:
        platform_evaluators (List[PlatformEvaluatorType[T]]): The list of platform evaluators to sanitize.

    Raises:
        ValueError: If multiple evaluators with the same name are found.
    """
    if platform_evaluators is None:
        return
    names_encountered = set[str]()
    for evaluator in platform_evaluators:
        if evaluator.name in names_encountered:
            raise ValueError(
                f'Multiple evaluators with the same name "{evaluator.name}" found',
                json.dumps(
                    {"allEvaluatorNames": [e.name for e in platform_evaluators]},
                    indent=2,
                ),
            )
        names_encountered.add(evaluator.name)


def sanitize_data(
    data_to_sanitize: DataValue[Any],
    against_data_structure: Optional[DataStructure],
) -> None:
    """
    Sanitize the input data against a given data structure.

    Args:
        data_to_sanitize (DataValue[T]): The data to sanitize.
        against_data_structure (Optional[DataStructure]): The data structure to validate against.

    Raises:
        ValueError: If the data does not conform to the expected structure or contains invalid values.
    """
    if data_to_sanitize:
        if against_data_structure and not isinstance(data_to_sanitize, str):
            for entry in data_to_sanitize:
                for key, value in entry.items():
                    if (
                        key in against_data_structure
                        and against_data_structure[key] == "INPUT"
                    ):
                        if not isinstance(value, str):
                            raise ValueError(
                                f'Input column "{key}" has a data entry which is not a string',
                                json.dumps({"dataEntry": entry}, indent=2),
                            )
                    elif (
                        key in against_data_structure
                        and against_data_structure[key] == "EXPECTED_OUTPUT"
                    ):
                        if not isinstance(value, str):
                            raise ValueError(
                                f'Expected output column "{key}" has a data entry which is not a string',
                                json.dumps({"dataEntry": entry}, indent=2),
                            )
                    elif key in against_data_structure and against_data_structure[
                        key
                    ] in [
                        "CONTEXT_TO_EVALUATE",
                        "VARIABLE",
                    ]:
                        if not isinstance(value, str) and not (
                            isinstance(value, list)
                            and all(isinstance(v, str) for v in value)
                        ):
                            raise ValueError(
                                f'Column "{key}" has a data entry which is not a string or an array of strings',
                                json.dumps({"dataEntry": entry}, indent=2),
                            )
                    elif (
                        key in against_data_structure
                        and against_data_structure[key] == "NULLABLE_VARIABLE"
                    ):
                        if (
                            value is not None
                            and not isinstance(value, str)
                            and not (
                                isinstance(value, list)
                                and all(isinstance(v, str) for v in value)
                            )
                        ):
                            raise ValueError(
                                f'Nullable variable column "{key}" has a data entry which is not null, a string or an array of strings',
                                json.dumps({"dataEntry": entry}, indent=2),
                            )
                    else:
                        raise ValueError(
                            f'Unknown column type for column "{key}"',
                            json.dumps(
                                {
                                    "dataStructure": against_data_structure,
                                    "dataEntry": entry,
                                },
                                indent=2,
                            ),
                        )
    elif not isinstance(data_to_sanitize, str):
        raise ValueError(
            "Data structure is not provided and data argument is not a datasetId(string)",
            json.dumps({"data": data_to_sanitize}, indent=2),
        )


def sanitize_data_structure(data_structure: Optional[DataStructure]) -> None:
    """
    Sanitize the data structure to ensure it contains valid and unique column types.

    Args:
        data_structure (Optional[DataStructure]): The data structure to sanitize.

    Raises:
        ValueError: If the data structure contains invalid or duplicate column types.
    """
    encountered_input = False
    encountered_expected_output = False
    encountered_context_to_evaluate = False

    if data_structure:
        for value in data_structure.values():
            if value == "INPUT":
                if encountered_input:
                    raise ValueError(
                        "Data structure contains more than one input",
                        json.dumps({"dataStructure": data_structure}, indent=2),
                    )
                else:
                    encountered_input = True
            elif value == "EXPECTED_OUTPUT":
                if encountered_expected_output:
                    raise ValueError(
                        "Data structure contains more than one expectedOutput",
                        json.dumps({"dataStructure": data_structure}, indent=2),
                    )
                else:
                    encountered_expected_output = True
            elif value == "CONTEXT_TO_EVALUATE":
                if encountered_context_to_evaluate:
                    raise ValueError(
                        "Data structure contains more than one contextToEvaluate",
                        json.dumps({"dataStructure": data_structure}, indent=2),
                    )
                else:
                    encountered_context_to_evaluate = True


@dataclass
class ProcessedEntry:
    entry: TestRunEntry
    meta: Optional[YieldedOutputMeta] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "entry": self.entry.to_dict(),
            "meta": self.meta.to_dict() if self.meta else None,
        }


@final
class TestRunBuilder(Generic[T]):
    """
    Builder for test runs.
    """

    def __init__(self, config: TestRunConfig[Any]) -> None:
        """
        Constructor
        """
        self._config = config
        # attaching default data structure
        self._config.data_structure = {
            "INPUT": "input",
            "EXPECTED_OUTPUT": "expected_output",
            "CONTEXT_TO_EVALUATE": "context_to_evaluate",
        }
        self._maxim_apis = MaximAPI(config.base_url, config.api_key)

    def __process_entry(
        self,
        index: int,
        keys: dict[str, Optional[str]],
        output_function: Optional[
            Callable[[DataValue[Any]], Union[YieldedOutput, Awaitable[YieldedOutput]]]
        ],
        get_row: Callable[[int], Optional[dict[str, Any]]],
        logger: TestRunLogger,
    ) -> ProcessedEntry:
        """
        Process a single test run entry

        Args:
            index (int): The index of the entry
            keys (dict[str, Optional[str]]): Mapping of column names to keys in the data
            output_function (Callable[[dict[str, Any]], YieldedOutput]): Function to generate output
            get_row (Callable[[int], Optional[dict[str, Any]]]): Function to retrieve a row from the dataset
            logger (TestRunLogger): Logger instance

        Returns:
            ProcessedEntry: Contains processed entry and metadata
        """
        input = None
        expected_output = None
        context_to_evaluate = None
        row = get_row(index)
        if row is None:
            raise ValueError(f"Dataset entry {index} is missing")
        if "input" in keys and keys["input"] is not None and keys["input"] in row:
            input = row[keys["input"]] or str(row[keys["input"]]) or None
        if (
            "expected_output" in keys
            and keys["expected_output"] is not None
            and keys["expected_output"] in row
        ):
            expected_output = (
                row[keys["expected_output"]]
                or str(row[keys["expected_output"]])
                or None
            )
        if (
            "context_to_evaluate" in keys
            and keys["context_to_evaluate"] is not None
            and keys["context_to_evaluate"] in row
        ):
            context_to_evaluate = (
                row[keys["context_to_evaluate"]]
                or str(row[keys["context_to_evaluate"]])
                or None
            )
        output: Optional[
            Union[Awaitable[YieldedOutput], YieldedOutput, Dict[str, Any]]
        ] = None
        if output_function is not None:
            output = output_function(row)

        if isinstance(output, Awaitable):
            output = output.result()
        if isinstance(output, dict):
            output = YieldedOutput(
                data=str(output.get("data", "")),
                retrieved_context_to_evaluate=output.get(
                    "retrieved_context_to_evaluate"
                )
                or None,
                meta=output.get("meta") or None,
            )
        if output is not None:
            if (
                output.retrieved_context_to_evaluate is not None
                and context_to_evaluate is not None
            ):
                logger.info(
                    "Overriding context_to_evaluate from output over dataset entry"
                )
                context_to_evaluate = output.retrieved_context_to_evaluate
        return ProcessedEntry(
            entry=TestRunEntry(
                output=output.data if output is not None else None,
                input=input,
                expected_output=expected_output,
                context_to_evaluate=context_to_evaluate,
            ),
            meta=output.meta if output is not None else None,
        )

    def with_data_structure(self, data: T) -> "TestRunBuilder[T]":
        """
        Set the data structure for the test run

        Args:
            data (T): The data structure to use

        Returns:
            TestRunBuilder[T]: The current TestRunBuilder instance for method chaining
        """
        sanitize_data_structure(data)
        self._config.data_structure = data
        return self

    def with_data(self, data: DataValue[T]) -> "TestRunBuilder[T]":
        """
        Set the data for the test run

        Args:
            data (DataValue[T]): The data to use

        Returns:
            TestRunBuilder[T]: The current TestRunBuilder instance for method chaining
        """
        sanitize_data(data, self._config.data_structure)
        self._config.data = data
        return self

    def with_evaluators(self, *evaluators: str) -> "TestRunBuilder[T]":
        """
        Add evaluators to the test run

        Args:
            *evaluators (str): The evaluators to add

        Returns:
            TestRunBuilder[T]: The current TestRunBuilder instance for method chaining
        """
        final_evaluators = self._config.platform_evaluators or []
        for evaluator in evaluators:
            final_evaluators.append(
                PlatformEvaluatorType(name=evaluator, type="platform")
            )
        sanitize_evaluators(final_evaluators)
        self._config.platform_evaluators = final_evaluators
        return self

    def with_human_evaluation_config(
        self, config: HumanEvaluationConfig
    ) -> "TestRunBuilder[T]":
        """
        Set the human evaluation configuration for the test run

        Args:
            config (HumanEvaluationConfig): The human evaluation configuration to use

        Returns:
            TestRunBuilder[T]: The current TestRunBuilder instance for method chaining
        """
        email_regex = re.compile(
            r"^(?!\.)(?!.*\.\.)([A-Z0-9_\'+\-\.]*)[A-Z0-9_+-]@([A-Z0-9][A-Z0-9\-]*\.)+[A-Z]{2,}$",
            re.IGNORECASE,
        )
        invalid_emails = [
            email for email in config.emails if not email_regex.match(email)
        ]
        if len(invalid_emails) > 0:
            raise ValueError(f"Invalid email addresses: {', '.join(invalid_emails)}")
        self._config.human_evaluation_config = config
        return self

    def with_workflow_id(self, workflow_id: str) -> "TestRunBuilder[T]":
        """
        Set the workflow ID for the test run

        Args:
            workflow_id (str): The ID of the workflow to use

        Returns:
            TestRunBuilder[T]: The current TestRunBuilder instance for method chaining

        Raises:
            ValueError: If a prompt version ID or output function is already set for this run builder
        """
        if self._config.prompt_version_id is not None:
            raise ValueError(
                "Prompt version id is already set for this run builder. You can use either of with_prompt_version_id or with_workflow_id or yields_output in a test run."
            )
        if self._config.output_function is not None:
            raise ValueError(
                "yeilds_output is already set for this run builder. You can use either of with_prompt_version_id or with_workflow_id or yields_output in a test run."
            )
        self._config.workflow_id = workflow_id
        return self

    def with_prompt_version_id(self, prompt_version_id: str) -> "TestRunBuilder[T]":
        """
        Set the prompt version ID for the test run

        Args:
            prompt_version_id (str): The ID of the prompt version to use

        Returns:
            TestRunBuilder[T]: The current TestRunBuilder instance for method chaining

        Raises:
            ValueError: If a workflow ID or output function is already set for this run builder
        """
        if self._config.workflow_id is not None:
            raise ValueError(
                "Workflow id is already set for this run builder. You can use either of with_prompt_version_id or with_workflow_id or yields_output in a test run."
            )
        if self._config.output_function is not None:
            raise ValueError(
                "yields_output is already set for this run builder. You can use either of with_prompt_version_id or with_workflow_id or yields_output in a test run."
            )
        self._config.prompt_version_id = prompt_version_id
        return self

    def yields_output(
        self,
        output_function: Callable[
            [DataValue[T]], Union[YieldedOutput, Awaitable[YieldedOutput]]
        ],
    ) -> "TestRunBuilder[T]":
        """
        Set the output function for the test run

        Args:
            output_function (Callable[[T], Union[YieldedOutput, Awaitable[YieldedOutput]]]): The output function to use

        Returns:
            TestRunBuilder[T]: The current TestRunBuilder instance for method chaining

        Raises:
            ValueError: If a workflow ID or prompt version ID is already set for this run builder
        """
        if self._config.workflow_id is not None:
            raise ValueError(
                "Workflow id is already set for this run builder. You can use either of with_prompt_version_id or with_workflow_id or yields_output in a test run."
            )
        if self._config.prompt_version_id is not None:
            raise ValueError(
                "Prompt version id is already set for this run builder. You can use either of with_prompt_version_id or with_workflow_id or yields_output in a test run."
            )
        self._config.output_function = output_function
        return self

    def with_concurrency(self, concurrency: int) -> "TestRunBuilder[T]":
        """
        Set the concurrency level for the test run

        Args:
            concurrency (int): The concurrency level to use

        Returns:
            TestRunBuilder[T]: The current TestRunBuilder instance for method chaining
        """
        self._config.concurrency = concurrency
        return self

    def with_logger(self, logger: TestRunLogger) -> "TestRunBuilder[T]":
        """
        Set the logger for the test run

        Args:
            logger (TestRunLogger): The logger to use

        Returns:
            TestRunBuilder[T]: The current TestRunBuilder instance for method chaining
        """
        self._config.logger = logger
        return self

    def _run_test_with_local_data(
        self,
        test_run: TestRun,
        get_row: Callable[[int], Optional[Dict[str, Any]]],
        on_entry_failed: Callable[[int], None],
        on_dataset_finished: Callable[[], None],
    ):
        """
        Run the test with local data

        Args:
            test_run (TestRun): The test run to execute
            get_row (Callable[[int], Optional[Dict[str, Any]]]): Function to retrieve a row from the dataset
            on_entry_failed (Callable[[int], None]): Callback for when an entry fails
            on_dataset_finished (Callable[[], None]): Callback for when the dataset is finished
        """
        semaphore = Semaphore.get(
            f"test_run:{test_run.workspace_id}:{test_run.id}",
            self._config.concurrency or 10,
        )
        data_structure = self._config.data_structure
        try:
            input_key = get_all_keys_by_value(data_structure, "INPUT")[0]
        except IndexError:
            input_key = None
        try:
            expectedOutputKey = get_all_keys_by_value(
                data_structure, "EXPECTED_OUTPUT"
            )[0]
        except IndexError:
            expectedOutputKey = None
        try:
            contextToEvaluateKey = get_all_keys_by_value(
                data_structure, "CONTEXT_TO_EVALUATE"
            )[0]
        except IndexError:
            contextToEvaluateKey = None

        def process_row(index: int, row: Dict[str, Any]) -> None:
            try:
                result = self.__process_entry(
                    index=index,
                    keys={
                        "input": input_key,
                        "expected_output": expectedOutputKey,
                        "context_to_evaluate": contextToEvaluateKey,
                    },
                    output_function=self._config.output_function,
                    get_row=lambda index: row,
                    logger=self._config.logger,
                )
                # pushing this entry to test run
                self._maxim_apis.push_test_run_entry(
                    test_run=test_run,
                    entry=result.entry,
                    run_config=(
                        {
                            "cost": (
                                result.meta.cost.to_dict()
                                if result.meta.cost is not None
                                else None
                            ),
                            "usage": (
                                result.meta.usage.to_dict()
                                if result.meta.usage is not None
                                else None
                            ),
                        }
                        if result.meta is not None
                        else None
                    ),
                )
            except Exception as e:
                self._config.logger.error(
                    f"Error while running data entry at index [{index}]", e
                )
                on_entry_failed(index)

        def process_all_entries() -> None:
            threads = []
            index = 0
            while True:
                try:
                    semaphore.acquire()
                    # getting the entry
                    row = get_row(index)
                    if row is None:
                        on_dataset_finished()
                        break
                    # sanitizing data
                    try:
                        sanitize_data([row], self._config.data_structure)
                    except ValueError as e:
                        self._config.logger.error(
                            f"Invalid data entry at index [{index}]", e
                        )
                        on_entry_failed(index)
                        continue
                    index += 1
                    thread = threading.Thread(target=process_row, args=(index, row))
                    thread.start()
                    threads.append(thread)
                except Exception as e:
                    self._config.logger.error(
                        f"Error while running data entry at index [{index}]", e
                    )
                    on_entry_failed(index)
                finally:
                    semaphore.release()

        thread = threading.Thread(target=process_all_entries, args=())
        thread.start()

    def _run_test_with_dataset_id(
        self,
        test_run: TestRun,
        dataset_id: str,
        on_entry_failed: Callable[[int], None],
        on_dataset_finished: Callable[[], None],
    ) -> None:
        """
        Run the test with a dataset ID

        Args:
            test_run (TestRun): The test run to execute
            dataset_id (str): The ID of the dataset to use
            on_entry_failed (Callable[[int], None]): Callback for when an entry fails
            on_dataset_finished (Callable[[], None]): Callback for when the dataset is finished
        """
        semaphore = Semaphore.get(
            f"test_run:{test_run.workspace_id}:{test_run.id}",
            self._config.concurrency or 10,
        )
        data_structure = self._maxim_apis.get_dataset_structure(dataset_id)
        self._maxim_apis.attach_dataset_to_test_run(
            test_run_id=test_run.id, dataset_id=dataset_id
        )
        try:
            input_key = get_all_keys_by_value(data_structure, "INPUT")[0]
        except IndexError:
            input_key = None
        try:
            expectedOutputKey = get_all_keys_by_value(
                data_structure, "EXPECTED_OUTPUT"
            )[0]
        except IndexError:
            expectedOutputKey = None
        try:
            contextToEvaluateKey = get_all_keys_by_value(
                data_structure, "CONTEXT_TO_EVALUATE"
            )[0]
        except IndexError:
            contextToEvaluateKey = None

        def process_dataset_entry(index: int, row: DatasetRow, dataset_id: str) -> None:
            try:
                # processing the entry
                result = self.__process_entry(
                    index=index,
                    keys={
                        "input": input_key,
                        "expected_output": expectedOutputKey,
                        "context_to_evaluate": contextToEvaluateKey,
                    },
                    output_function=self._config.output_function,
                    get_row=lambda index: row.data,
                    logger=self._config.logger,
                )
                # pushing this entry to test run
                self._maxim_apis.push_test_run_entry(
                    test_run=TestRunWithDatasetEntry(
                        test_run=test_run,
                        dataset_id=dataset_id,
                        dataset_entry_id=row.id,
                    ),
                    entry=result.entry,
                    run_config=(
                        {
                            "cost": (
                                result.meta.cost.to_dict()
                                if result.meta.cost is not None
                                else None
                            ),
                            "usage": (
                                result.meta.usage.to_dict()
                                if result.meta.usage is not None
                                else None
                            ),
                        }
                        if result.meta
                        else None
                    ),
                )
            except Exception as e:
                self._config.logger.error(
                    f"Error while running data entry at index [{index}]", e
                )
                on_entry_failed(index)
                raise e

        def process_all_dataset_entries(dataset_id: str) -> None:
            threads = []
            index = 0
            while True:
                try:
                    semaphore.acquire()
                    # getting the entry
                    row = self._maxim_apis.get_dataset_row(dataset_id, index)
                    if row is None:
                        on_dataset_finished()
                        break
                    index += 1
                    thread = threading.Thread(
                        target=process_dataset_entry, args=(index, row, dataset_id)
                    )
                    thread.start()
                    threads.append(thread)
                except Exception as e:
                    self._config.logger.error(
                        f"Error while running data entry at index [{index}]", e
                    )
                    on_entry_failed(index)
                finally:
                    semaphore.release()

            for thread in threads:
                thread.join()

        thread = threading.Thread(
            target=process_all_dataset_entries, args=(dataset_id,)
        )
        thread.start()

    def run(self, timeout_in_minutes: Optional[int] = 10) -> Optional[RunResult]:
        """
        Run the test

        Args:
            timeout_in_minutes (Optional[int]): The timeout in minutes. Defaults to 10.

        Returns:
            RunResult: The result of the test run
        """
        errors: list[str] = []
        if self._config.name == "":
            errors.append("Name is required to run a test.")
        if self._config.in_workspace_id == "":
            errors.append("Workspace id is required to run a test.")
        if (
            self._config.output_function is None
            and self._config.workflow_id is None
            and self._config.prompt_version_id is None
        ):
            errors.append(
                "One of output function (by calling yields_output) or workflow id (by calling with_workflow_id) or prompt version id (by calling with_prompt_version_id) is required to run a test."
            )
        if self._config.data is None:
            errors.append("Dataset id is required to run a test.")
        if len(errors) > 0:
            raise ValueError("Missing required configuration for test\n".join(errors))
        sanitize_data_structure(self._config.data_structure)
        if isinstance(self._config.data, List):
            sanitize_data(self._config.data, self._config.data_structure)
        sanitize_evaluators(self._config.platform_evaluators)
        platform_evaluator_configs: List[Evaluator] = []

        for evaluator in self._config.platform_evaluators or []:
            evaluator_config = self._maxim_apis.fetch_platform_evaluator(
                name=evaluator.name, in_workspace_id=self._config.in_workspace_id
            )
            platform_evaluator_configs.append(evaluator_config)
        if any(
            evaluator.type.value == EvaluatorType.HUMAN.value
            for evaluator in platform_evaluator_configs
        ):
            if self._config.human_evaluation_config is None:
                raise ValueError(
                    "Human evaluator found in evaluators, but no human evaluation config was provided."
                )

        name = self._config.name
        data = self._config.data
        workspace_id = self._config.in_workspace_id
        human_evaluation_config = self._config.human_evaluation_config
        failed_entry_indices = []
        all_entries_processed = threading.Event()

        def mark_all_entries_processed() -> None:
            nonlocal all_entries_processed
            all_entries_processed.set()

        try:
            self._config.logger.info(f"Creating test run {name}")
            test_run = self._maxim_apis.create_test_run(
                name=name,
                workspace_id=workspace_id,
                run_type=RunType.SINGLE,
                workflow_id=self._config.workflow_id,
                prompt_version_id=self._config.prompt_version_id,
                evaluator_config=platform_evaluator_configs,
                human_evaluation_config=human_evaluation_config or None,
            )
            if data is not None:
                if isinstance(data, str):
                    self._run_test_with_dataset_id(
                        test_run=test_run,
                        dataset_id=data,
                        on_entry_failed=failed_entry_indices.append,
                        on_dataset_finished=mark_all_entries_processed,
                    )
                elif isinstance(data, list):
                    self._run_test_with_local_data(
                        test_run,
                        lambda index: data[index] if index < len(data) else None,
                        failed_entry_indices.append,
                        mark_all_entries_processed,
                    )
                elif isinstance(data, Callable):
                    self._run_test_with_local_data(
                        test_run,
                        data,
                        failed_entry_indices.append,
                        mark_all_entries_processed,
                    )
                else:
                    raise ValueError("Invalid data")

            self._maxim_apis.mark_test_run_processed(test_run.id)
            self._config.logger.info(
                f"You can view your test run here: {self._config.base_url}/workspace/{self._config.in_workspace_id}/testrun/{test_run.id}"
            )
            self._config.logger.info(
                "You can safely quit this session or wait to see the final output in console."
            )
            poll_count = 0
            polling_interval = calculate_polling_interval(
                timeout_in_minutes or 10,
                is_ai_evaluator_in_use=any(
                    e.type == "AI" for e in platform_evaluator_configs
                )
                or False,
            )
            max_iterations = math.ceil(
                (round(timeout_in_minutes or 10) * 60) / polling_interval
            )
            self._config.logger.info("Waiting for test run to complete...")
            self._config.logger.info(f"Polling interval: {polling_interval} seconds")
            status: Optional[TestRunStatus] = None
            while True:
                status = self._maxim_apis.get_test_run_status(test_run.id)
                status_dict = status.to_dict()
                status_line = " | ".join(
                    f"{key}: {value}"
                    for key, value in status_dict.items()
                    if key != "testRunStatus"
                )
                box_width = max(50, len(status_line) + 4)
                header_width = len(f" Test run status: {status.test_run_status.value} ")
                box_width = max(box_width, header_width + 4)

                header = f" Test run status: {status.test_run_status.value} ".center(
                    box_width
                )
                self._config.logger.info("┌" + "─" * box_width + "┐")
                self._config.logger.info(f"│{header}│")
                self._config.logger.info("├" + "─" * box_width + "┤")

                status_line = " | ".join(
                    f"{key}: {value}"
                    for key, value in status_dict.items()
                    if key != "testRunStatus"
                )
                self._config.logger.info(f"│ {status_line:<{box_width-2}} │")
                self._config.logger.info("└" + "─" * box_width + "┘\n")
                if poll_count > max_iterations:
                    raise Exception(
                        f"Test run is taking over timeout period ({round(timeout_in_minutes or 10)} minutes) to complete, please check the report on our web portal directly: {self._config.base_url}/workspace/{self._config.in_workspace_id}/testrun/{test_run.id}"
                    )

                # Test run is failed - we break the loop
                if (
                    status.test_run_status.value == RunStatus.FAILED.value
                    or status.test_run_status.value == RunStatus.STOPPED.value
                ):
                    break

                if (
                    status.test_run_status.value == RunStatus.COMPLETE.value
                    and all_entries_processed.is_set()
                ):
                    # We will check if we sent all the entries
                    if status.total_entries != 0 and (
                        status.total_entries
                        == status.completed_entries
                        + status.failed_entries
                        + status.stopped_entries
                    ):
                        self._config.logger.info(
                            "All entries processed. Test run completed."
                        )
                        break
                # Polling again
                time.sleep(polling_interval)
                poll_count += 1

            if status.test_run_status.value == RunStatus.FAILED:
                raise Exception(
                    f"Test run failed, please check the report on our web portal: {self._config.base_url}/workspace/{self._config.in_workspace_id}/testrun/{test_run.id}"
                )

            if status.test_run_status.value == RunStatus.STOPPED:
                raise Exception(
                    f"Test run was stopped, please check the report on our web portal: {self._config.base_url}/workspace/{self._config.in_workspace_id}/testrun/{test_run.id}"
                )

            test_run_result = self._maxim_apis.get_test_run_final_result(test_run.id)
            test_run_result.link = self._config.base_url + test_run_result.link
            self._config.logger.info(
                f'Test run "{name}" completed successfully!🎉 \nView the report here: {test_run_result.link}'
            )
            return RunResult(
                test_run_result=test_run_result,
                failed_entry_indices=failed_entry_indices,
            )

        except Exception as e:
            self._config.logger.error(f"💥 Error: {e}", e)
