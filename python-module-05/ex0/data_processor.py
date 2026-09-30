#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   data_processor.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/21 12:38:14 by mpinto-l            #+#    #+#            #
#   Updated: 2026/09/30 15:36:09 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._total_ingested: int = 0
        self._data_stored: list[tuple[int, str]] = []

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: Any) -> None:
        ...

    def output(self) -> tuple[int, str]:
        if self._data_stored:
            return self._data_stored.pop(0)
        raise IndexError("No data available to output.")


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for item in data:
                if (
                    not isinstance(item, (int, float))
                    or isinstance(item, bool)
                ):
                    return False
            return True
        else:
            return (
                isinstance(data, (int, float))
                and not isinstance(data, bool)
                )

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError('Improper numeric data.')
        values_to_ingest: list[int | float]
        if isinstance(data, list):
            values_to_ingest = data
        else:
            values_to_ingest = [data]
        for value in values_to_ingest:
            self._data_stored.append((self._total_ingested, str(value)))
            self._total_ingested += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, (str)):
                    return False
            return True
        else:
            return isinstance(data, (str))

    def ingest(self, data: str) -> None:
        if not self.validate(data):
            raise ValueError('Improper text data.')
        values_to_ingest: list[str]
        if isinstance(data, list):
            values_to_ingest = data
        else:
            values_to_ingest = [data]
        for value in values_to_ingest:
            self._data_stored.append((self._total_ingested, value))
            self._total_ingested += 1


class LogProcesssor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return "log_level" in data and "log_message" in data
        if isinstance(data, list):
            return all(
                isinstance(item, dict)
                and "log_level" in item
                and "log_message" in item
                for item in data
            )
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError('Improper log message')
        values_to_ingest: list[dict[str, str]]
        if isinstance(data, list):
            values_to_ingest = data
        else:
            values_to_ingest = [data]
        for value in values_to_ingest:
            formated_message = f"{value['log_level']}: {value['log_message']}"
            self._data_stored.append((self._total_ingested, formated_message))
            self._total_ingested += 1


def test_numeric() -> None:
    numeric = NumericProcessor()

    print("Testing Numeric Processor...")
    print(f"Trying to validate input '42': {numeric.validate(42)}")
    print(f"Trying to validate input 'Hello': {numeric.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest("foo")
    except ValueError as error:
        print(f'Got exception: {error}')

    numeric_data: list[int | float] = [1, 2, 3, 4, 5]
    print(f"Processing Data: {numeric_data}")
    numeric.ingest(numeric_data)
    print('Extracting 3 values...')
    for _ in range(3):
        index, value = numeric.output()
        print(f"Numeric value {index}: {value}")


def test_text() -> None:
    text = TextProcessor()

    print('\nTesting Text Processor...')
    print(f"Trying to validate input '42': {text.validate(42)}")
    text_data: list[str] = ['Hello', 'Nexus', 'World']
    print(f'Processing data: {text_data}')
    text.ingest(text_data)
    print('Extracting 1 value...')
    for _ in range(1):
        index, value = text.output()
        print(f'Text value: {index}: {value}')


def test_log() -> None:
    log = LogProcesssor()

    print('\nTesting Log Processor...')
    print(f"Trying to validate input 'Hello': {log.validate('Hello')}")
    log_data = [{
                    "log_level": "NOTICE",
                    "log_message": "Connection to server"
                },
                {
                    "log_level": "ERROR",
                    "log_message": "Unauthorized access!!"
                }]
    print(f'Processing data: {log_data}')
    log.ingest(log_data)
    print('Extracting 2 values...')
    for _ in range(2):
        index, message = log.output()
        print(f'Log entry {index}: {message}')


def test_data() -> None:
    print('=== Code Nexus - Data Processor ===\n')
    test_numeric()
    test_text()
    test_log()


if __name__ == "__main__":
    test_data()
