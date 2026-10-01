#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   data_pipeline.py                                     :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/21 12:38:14 by mpinto-l            #+#    #+#            #
#   Updated: 2026/10/01 13:48:55 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from abc import ABC, abstractmethod
from typing import Any, Protocol


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
            raise ValueError('Improper text data')
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


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        if not data:
            return

        values = [item[1] for item in data]
        csv_line = ",".join(values)
        print("CSV Output:")
        print(csv_line)


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        if not data:
            return

        json_entries = [f'"item_{rank}": "{val}"' for rank, val in data]
        formatted_json = "{" + ", ".join(json_entries) + "}"
        print("JSON Output:")
        print(formatted_json)


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
        print("\n== DataStream statistics ==")
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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self._processors:
            exported_items: list[tuple[int, str]] = []

            for _ in range(nb):
                if processor.get_data_stored():
                    exported_items.append(processor.output())
                else:
                    break
            if exported_items:
                plugin.process_output(exported_items)


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===")

    print("\nInitialize Data Stream...\n")
    data_stream = DataStream()
    data_stream.print_processors_stats()

    print("\nRegistering Processors")
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    data_stream.register_processor(numeric)
    data_stream.register_processor(text)
    data_stream.register_processor(log)

    batch1: list[Any] = [
        "Hello World",
        [1.25, 4, 5.23],
        [
            {
                "log_level": "Warning",
                "log_message": "Telnet access! Use ssh instead"
            },
            {
                "log_level": "INFO",
                "log_message": "User yann is connected!!!"
            }
        ],
        42,
        ["Hi", "five"]
        ]

    print(f"\nSend first batch of data on stream: {batch1}")
    data_stream.process_stream(batch1)
    data_stream.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVExportPlugin()
    data_stream.output_pipeline(3, csv_plugin)
    data_stream.print_processors_stats()

    batch2: list[Any] = [
        21,
        ["I love AI", "banana", "item_4"],
        [
            {
                "log_level": "NOTICE",
                "log_message": "Password expires in 10 days",
            },
        ],
        [4, 8, 15, 16, 23, 42],
        "Hello, it's me."
    ]

    print(f"\nSend another batch of data: {batch2}")
    data_stream.process_stream(batch2)
    data_stream.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONExportPlugin()
    data_stream.output_pipeline(5, json_plugin)

    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()
