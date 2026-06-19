#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   main.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: zo-rakot <zo-rakot@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/18 05:30:13 by zo-rakot            #+#    #+#            #
#   Updated: 2026/06/18 05:32:21 by zo-rakot           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys
from config_parser import ConfigParser
from maze import Maze
from generate import generate
from solver import solve

if __name__ == "__main__":

    if len(sys.argv) != 2:
        raise ValueError("Usage: python3 main.py config.txt")

    config_file = sys.argv[1]

    parser = ConfigParser(config_file)
    config = parser.parse_file()

    maze = Maze(
        config["WIDTH"],
        config["HEIGHT"],
        config["ENTRY"],
        config["EXIT"]
    )

    generate(maze)
    path = solve(maze)
    maze.display(path)