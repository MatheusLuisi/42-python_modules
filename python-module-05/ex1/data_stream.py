#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   data_stream.py                                       :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/21 12:38:14 by mpinto-l            #+#    #+#            #
#   Updated: 2026/10/01 13:44:39 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.name = "DataProcessor"
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

    def get_data_stored(self) -> list[tuple[int, str]]:
        return self._data_stored

    def get_total_ingested(self) -> int:
        return self._total_ingested


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Numeric Processor"

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
            raise ValueError('Improper numeric data')
        values_to_ingest: list[int | float]
        if isinstance(data, list):
            values_to_ingest = data
        else:
            values_to_ingest = [data]
        for value in values_to_ingest:
            self._data_stored.append((self._total_ingested, str(value)))
            self._total_ingested += 1


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Text Processor"

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, (str)):
                    return False
            return True
        else:
            return isinstance(data, (str))

    def ingest(self, data: str | list[str]) -> None:
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


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Log Processor"

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
            formatted_message = f"{value['log_level']}: {value['log_message']}"
            self._data_stored.append((self._total_ingested, formatted_message))
            self._total_ingested += 1


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            for processor in self._processors:
                if processor.validate(element):
                    processor.ingest(element)
                    break
            else:
                print(f"DataStream error - Can't process element: {element}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for processor in self._processors:
            total = processor.get_total_ingested()
            remaining = len(processor.get_data_stored())
            print(
                f"{processor.name}: total {total} items processed, "
                f"remaining {remaining} on processor"
            )


def test_data() -> None:
    print('=== Code Nexus - Data Stream ===\n')

    print('Initialize Data Stream...')
    data_stream = DataStream()
    data_stream.print_processors_stats()

    print("Registering Numeric Processor")
    numeric = NumericProcessor()
    data_stream.register_processor(numeric)

    batch: list[Any] = [
        "Hello World",
        [1.25, 4, 5.23],
        [
            {
                "log_level": "NOTICE",
                "log_message": "Connection to server"
            },
            {
                "log_level": "ERROR",
                "log_message": "Unauthorized access!!!"
            }
        ],
        42,
        ["Hi", "five"]
    ]

    print(f"\nSend first batch of data on stream: {batch}")
    data_stream.process_stream(batch)
    data_stream.print_processors_stats()

    print("\nRegistering other data processors")
    text = TextProcessor()
    data_stream.register_processor(text)
    log = LogProcessor()
    data_stream.register_processor(log)

    print("Send the same batch again")
    data_stream.process_stream(batch)
    data_stream.print_processors_stats()

    print(
        "\nConsume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )

    for _ in range(3):
        numeric.output()

    for _ in range(2):
        text.output()

    for _ in range(1):
        log.output()

    data_stream.print_processors_stats()


if __name__ == "__main__":
    test_data()
