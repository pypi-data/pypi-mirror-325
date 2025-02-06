import asyncio
import os
import sqlite3
from dataclasses import dataclass
from datetime import datetime
from functools import partial
from typing import List, Tuple, Any, Optional

from .types import DatabaseLocation, memory_database_location, ExperimentConfig, InputType, OutputType


@dataclass
class Experiment:
    validator_id: str
    validator_name: str
    input: str
    output: str
    timestamp: datetime
    predicate_result: bool
    confidence_level: float


class CatDB:
    table_name = "experiment_run_results"

    def __init__(self, location: DatabaseLocation) -> None:
        self.location = location
        self._init_db()

    @property
    def table_create_query(self) -> str:
        return f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                experiment_id TEXT NOT NULL,
                experiment_run_id TEXT NOT NULL,
                validator_id TEXT NOT NULL,
                validator_name TEXT NOT NULL,
                input TEXT NOT NULL,
                output TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
                predicate_result BOOLEAN NOT NULL,
                confidence_level REAL NOT NULL
            )
        """

    @property
    def insert_query(self) -> str:
        return f"""
            INSERT INTO {self.table_name} (
                experiment_id,
                experiment_run_id,
                validator_id,
                validator_name,
                input,
                output,
                predicate_result,
                confidence_level
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """

    def _get_connection(self) -> sqlite3.Connection:
        if self.location == memory_database_location:
            conn = sqlite3.connect(':memory:')
        else:
            directory = os.path.dirname(self.location)
            if directory and not os.path.exists(directory):
                os.makedirs(directory, exist_ok=True)
            conn = sqlite3.connect(self.location)
        return conn

    def _init_db(self) -> None:
        conn = self._get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(self.table_create_query)
            conn.commit()
        finally:
            conn.close()

    async def execute_db_insert(self, values: Tuple[Any, ...]) -> None:
        def do_insert(_unused: None, values_to_insert: Tuple[Any, ...] = values) -> None:
            conn = self._get_connection()
            try:
                cursor = conn.cursor()
                cursor.execute(self.insert_query, values_to_insert)
                conn.commit()
            finally:
                conn.close()

        await asyncio.get_event_loop().run_in_executor(None, partial(do_insert, None))

    async def execute_experiment_run(self, config: ExperimentConfig[InputType, OutputType], run_id: str) -> List[None]:
        insert_value_sets = await self.insert_values(config, run_id)
        return await asyncio.gather(*[self.execute_db_insert(values) for values in insert_value_sets])

    async def execute_query(self, query: str, params: Optional[Tuple[Any, ...]] = None) -> List[Tuple[Any, ...]]:
        def do_query(_unused: None) -> List[Tuple[Any, ...]]:
            conn = self._get_connection()
            try:
                cursor = conn.cursor()
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                return cursor.fetchall()
            finally:
                conn.close()

        return await asyncio.get_event_loop().run_in_executor(None, partial(do_query, None))

    @staticmethod
    async def insert_values(config: ExperimentConfig[InputType, OutputType], run_id: str) -> List[Tuple[Any, ...]]:
        if hasattr(config, 'input'):
            output = await config.output(config.input)  # type: ignore
            values = [
                (
                    config.experiment_id,
                    str(run_id),
                    validator.id,
                    validator.name,
                    str(config.input),
                    str(output),
                    validator.predicate(config.input, output),
                    validator.confidence_level
                )
                for validator in config.validators
            ]
        else:
            output = await config.output()  # type: ignore
            values = [
                (
                    config.experiment_id,
                    str(run_id),
                    validator.id,
                    validator.name,
                    '',
                    str(output),
                    validator.predicate(output),
                    validator.confidence_level
                )
                for validator in config.validators
            ]

        return values
