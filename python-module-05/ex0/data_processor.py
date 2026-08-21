#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   data_processor.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/21 12:38:14 by mpinto-l            #+#    #+#            #
#   Updated: 2026/08/21 14:20:02 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import abc
import typing

class DataProcessor(ABC):
    def __init__ (self, data):
        self.data = data

    @abstractmethod
    def validate(self, data: Any) -> bool:

    @abstractmethod
    def ingest(self, data: Any) -> None:

    def output(self) -> tuple[int, str]:


class NumericProcessor(DataProcessor):
    def __init__ (self):
        super.__init__(self, data)

    def validate(self, data: Any) -> bool:

    def ingest(self, data: int | float) -> None:


class TextProcessor(DataProcessor):
    def __init__ (self):

    def validate(self, data: Any) -> bool:

    def ingest(self, data: str) -> None:


class LogProcesssor(DataProcessor):
    def __init__ (self):

    def validate(self, data: Any) -> bool:

    def ingest(self, data: dict) -> None:


def test_data() -> None:




if __name__ == "__main__":
    test_data()
