from typing import TypeVar, Union, Literal, Generic, Callable, Awaitable, Optional, List, Any

InputType = TypeVar("InputType")
OutputType = TypeVar("OutputType")

DatabaseLocation = Union[str, Literal["memory"]]
memory_database_location: Literal["memory"] = "memory"


class ExperimentConfig(Generic[InputType, OutputType]):
    def __init__(
        self,
        times_to_repeat: int,
        experiment_id: str,
        input: Optional[InputType] = None,
        output: Optional[Callable[[InputType], Awaitable[OutputType]]] = None,
        validators: Optional[List[Any]] = None,
    ) -> None:
        self.times_to_repeat = times_to_repeat
        self.experiment_id = experiment_id
        self.input = input
        self.output = output
        self.validators = validators if validators is not None else []
