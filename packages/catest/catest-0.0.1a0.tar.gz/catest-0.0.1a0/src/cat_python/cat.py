import asyncio
from typing import Generic, Callable, Awaitable, List, Any, Optional

from .db import CatDB
from .types import InputType, OutputType, DatabaseLocation, ExperimentConfig


class OutputValidator(Generic[OutputType]):
    def __init__(self, validator_id: str, name: str, confidence_level: float, predicate: Callable[[OutputType], bool]) -> None:
        self.id = validator_id
        self.name = name
        self.confidence_level = confidence_level
        self.predicate = predicate


class InputOutputValidator(Generic[InputType, OutputType]):
    def __init__(self, validator_id: str, name: str, confidence_level: float, predicate: Callable[[InputType, OutputType], bool]) -> None:
        self.id = validator_id
        self.name = name
        self.confidence_level = confidence_level
        self.predicate = predicate


class ExperimentRunner(Generic[InputType, OutputType]):
    def __init__(self, db: CatDB) -> None:
        self.db = db

    async def execute_experiment_run(self, config: ExperimentConfig[InputType, OutputType], run_id: str) -> List[Any]:
        insert_value_sets = await self.db.insert_values(config, run_id)
        return await asyncio.gather(*[self.db.execute_db_insert(values) for values in insert_value_sets])

    async def record_experiment(self, config: ExperimentConfig[InputType, OutputType], run_id: str) -> None:
        try:
            await self.execute_experiment_run(config, run_id)
        except Exception as error:
            print('Error in experiment:', error)
            raise


async def with_cat(location: DatabaseLocation, callback: Callable[[ExperimentRunner[Any, Any]], Awaitable[Any]]) -> Any:
    cats = ExperimentRunner[Any, Any](CatDB(location))
    return await callback(cats)
