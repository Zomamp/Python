#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   data_stream.py                                       :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: zo-rakot <zo-rakot@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/12 03:13:20 by zo-rakot            #+#    #+#            #
#   Updated: 2026/06/12 09:34:52 by zo-rakot           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


from abc import ABC, abstractmethod
import typing
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.storage: list[str] = []

    def output(self) -> tuple[int, str]:
        storage = self.storage[0]
        self.storage.pop(0)
        return (0, storage)

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: Any) -> None:
        ...


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return (True)
        if isinstance(data, list):
            return (all(isinstance(i, (int, float)) for i in data))
        return (False)

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise Exception("Improrer numeric data")
        if isinstance(data, list):
            for item in data:
                self.storage.append(str(item))
        else:
            self.storage.append(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return (True)
        if isinstance(data, list):
            return (all(isinstance(i, (str)) for i in data))
        return (False)

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise Exception("Improrer string data")
        if isinstance(data, list):
            for item in data:
                self.storage.append(item)
        else:
            self.storage.append(data)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return (
                all(
                    isinstance(i, str) and
                    isinstance(j, str)) for i, j in data.items()
                    )
        if isinstance(data, list):
            return (all(isinstance(i, str)) for i in data)
        return (False)

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")
        if isinstance(data, list):
            for item in data:
                self.storage.append(
                    f"{item['log_level']}: {item['log_message']}")
        else:
            self.storage.append(f"{data['log_level']: {item['log_message']}}")


class DataStream():
    def __init__(self):
        self.proces = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.proces.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        


if __name__ == "__main__":
    