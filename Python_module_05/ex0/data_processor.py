#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   data_processor.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: zo-rakot <zo-rakot@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/10 22:18:13 by zo-rakot            #+#    #+#            #
#   Updated: 2026/06/11 06:05:40 by zo-rakot           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


from abc import ABC, abstractmethod
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


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===\n")

    print("Testing Numeric Processor...\n")
    numeric = NumericProcessor()
    inp_num1 = 42
    inp_num2 = "Hello"
    print(
        f"Trying to validate input"
        f"'{inp_num1}': {numeric.validate(inp_num1)}")
    print(
        f"Trying to validate input"
        f"'{inp_num2}': {numeric.validate(inp_num2)}")

    try:
        inp_num3 = "foo"
        numeric.ingest(inp_num3)
    except Exception as e:
        print(f"Got exception: {e}")

    print("\nTesting Text Processor...")
    text = TextProcessor()
    print(f"Trying to validate input '42': {text.validate(42)}")
    text.ingest(['Hello', 'Nexus', 'World'])
    print("Processing data: ['Hello', 'Nexus', 'World']")
    print("Extracting 1 value...")
    rank, data = text.output()
    print(f"Text value 0: {data}")

    print("\nTesting Log Processor...")
    log = LogProcessor()
    print(f"Trying to validate input 'Hello': {log.validate('Hello')}")
    logs = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    log.ingest(logs)
    print(f"Processing data: {logs}")
    print("Extracting 2 values...")
    for i in range(2):
        rank, data = log.output()
        print(f"Log entry {i}: {data}")
