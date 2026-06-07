#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_command_quest.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: zo-rakot <zo-rakot@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/06 20:25:04 by zo-rakot            #+#    #+#            #
#   Updated: 2026/06/06 20:25:05 by zo-rakot           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


import sys


def printing_argv() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    lenght = len(sys.argv)
    if lenght < 2:
        print("No arguments provided!")
        print(f"Total arguments: {lenght}")
    else:
        print(f"Argument received: {lenght - 1}")
        i = 1
        while i < lenght:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
        print(f"Total arguments: {lenght}")


if __name__ == "__main__":
    printing_argv()
