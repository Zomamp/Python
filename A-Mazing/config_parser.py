#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   config_parser.py                                     :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: zo-rakot <zo-rakot@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/11 21:15:25 by zo-rakot            #+#    #+#            #
#   Updated: 2026/06/12 00:40:09 by zo-rakot           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


class Config_parser():

    REQUIRE_KEYS = [
        "WIDTH",
        "HEIGHT",
        "ENTRY",
        "EXIT",
        "OUTPUT_FILE",
        "PERFECT"
        ]

    def __init__(self, filepath: str) -> None:
        self.filepath = filepath
        self.storage: dict = {}

    def parse_file_open(self) -> dict:
        try:
            with open(self.filepath, "r") as f:
                for lign in f:
                    lign = lign.strip()

                    if not lign or lign.startswith("#"):
                        continue

                    if "=" not in lign:
                        raise Exception("Error not in lign")

                    key, value = lign.split("=", 1)
                    self.storage[key.strip()] = value.strip()
            self.validate()

        except Exception as e:
            print(f"Error: {e}")

        return (self.storage)

    def validate(self):
        for key in self.REQUIRE_KEYS:
            if key not in self.storage:
                raise Exception(f"Error the key is incomplete {key}")


if __name__ == "__main__":
    appel = Config_parser("config.txt")
    appel.parse_file_open()