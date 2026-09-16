#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   data_processor.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/21 12:38:14 by mpinto-l            #+#    #+#            #
#   Updated: 2026/09/15 11:48:41 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__ (self, data):
        self.data = data

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: Any) -> None:
        ...

    def output(self) -> tuple[int, str]:
        ...


class NumericProcessor(DataProcessor):
    def __init__ (self, data: Any):
        super.__init__(data)

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

    def ingest(self, data: int | float) -> None:
        if not self.validate(data):
            raise ValueError('Improper numeric data.')



class TextProcessor(DataProcessor):
    def __init__ (self, data: Any):
        super.__init__(data)

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, (str)):
                    return False
            return True
        else:
            return isinstance(data, (str))


    def ingest(self, data: str) -> None:



class LogProcesssor(DataProcessor):
    def __init__ (self, data: Any):
        super.__init__(data)

    def validate(self, data: Any) -> bool:
        return isinstance(data, dict)

    def ingest(self, data: dict) -> None:


def test_data() -> None:
    print("Testing Numeric Processor...")



if __name__ == "__main__":
    print('=== Code Nexus - Data Processor ===')
    test_data()
