#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   amazing.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: zo-rakot <zo-rakot@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/23 05:54:35 by zo-rakot            #+#    #+#            #
#   Updated: 2026/06/23 06:04:48 by zo-rakot           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

#!/usr/bin/env python3

import sys
import time

from config_parser import ConfigParser
from maze import Maze
from generate import generate
from solver import solve


def clear():
    print("\033[H\033[J", end="")


if __name__ == "__main__":

    if len(sys.argv) != 2:
        raise ValueError("Usage: python3 amazing.py config.txt")

    config_file = sys.argv[1]

    parser = ConfigParser(config_file)
    config = parser.parse_file()

    width = config["WIDTH"]
    height = config["HEIGHT"]
    entry = config["ENTRY"]
    exit = config["EXIT"]

    # ======================
    # INIT MAZE
    # ======================
    maze = Maze(width, height, entry, exit)
    generate(maze)

    while True:
        clear()
        maze.display()
        print("AMAZING BABY")
        print("\n===================")
        print("1) Regenerate maze")
        print("2) Solve maze")
        print("3) Showing Owner")
        print("q) Quit")
        print("===================")

        choice = input("> ").strip()

        # ======================
        # 1) REGENERATE
        # ======================
        if choice == "1":
            maze = Maze(width, height, entry, exit)
            generate(maze)

        # ======================
        # 2) SOLVE
        # ======================
        elif choice == "2":
            path = solve(maze)

            if path:
                # Nalako le display fa manao affichage anakiroa leizy
                # maze.display(path)
                input("\nPress Enter please ...")

        # ======================
        # 3) MAPISEO NY LOGIN
        # ======================
        # elif choice == "3":
            

        # ======================
        # QUIT
        # ======================
        elif choice == "q":
            break

        else:
            print("Invalid choice")
            time.sleep(0.5)