#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   amazing.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: zo-rakot <zo-rakot@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/23 05:54:35 by zo-rakot            #+#    #+#            #
#   Updated: 2026/06/25 06:21:37 by zo-rakot           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

#!/usr/bin/env python3

import sys
import time
import shutil

from config_parser import ConfigParser
from maze import Maze
from generate import generate
from solver import solve
from solver_BFS import solve_bfs

WALL = "\033[38;5;39m"   # bleu

def clear():
    print("\033[H\033[J", end="")


def get_width():
    return shutil.get_terminal_size((80, 20)).columns


def center(text: str) -> str:
    width = get_width()
    return text.center(width)

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
    last_path_42 = 0
    last_path = 0

    # ======================
    # INIT MAZE
    # ======================
    maze = Maze(width, height, entry, exit)
    generate(maze, perfect=config["PERFECT"])

    while True:
        print(center("🎉 Welcome to AMAZING 🧩✨"))
        print()
        print(center("COMMAND"))
        print(center("==================="))
        print(center("1) Regenerate maze"))
        print(center("2) Solve with DFS"))
        print(center("3) Solve with BFS"))
        print(center("4) Change color"))
        print(center("5) Change color 42"))
        print(center("q) Quit"))
        print(center("==================="))

        print(center("> "), end="", flush=True)
        choice = input()

        # ======================
        # 1) REGENERATE
        # ======================
        if choice == "1":
            maze = Maze(width, height, entry, exit)
            print(center("regenerate ."), end=" ", flush=True)
            time.sleep(1)
            print(center("regenerate .."), end=" ", flush=True)
            time.sleep(1)
            generate(maze, perfect=config["PERFECT"])

        # ======================
        # 2) SOLVE
        # ======================
        elif choice == "2":
            print(center("solving with DFS ."), end=" ", flush=True)
            time.sleep(1)
            print(center("solving with DFS .."), end=" ", flush=True)
            time.sleep(1)
            path = solve(maze)
            last_path = path
            last_path_42 = path

            if path:
                # Nalako le display fa manao affichage anakiroa leizy
                # maze.display(path)
                print(center("🎉 Congratulations, the solver is done! 🧩✨"), end=" ", flush=True)
                time.sleep(1)

        elif choice == "3":
            print(center("solving with BFS ."), end=" ", flush=True)
            time.sleep(1)
            print(center("solving with BFS .."), end=" ", flush=True)
            time.sleep(1)
            path = solve_bfs(maze)
            last_path = path
            last_path_42 = path

        elif choice == "4":
            Maze.change_color(maze)
            clear()
            maze.display(path=last_path)

        elif choice == "5":
            Maze.change_color_42(maze)
            clear()
            maze.display(path=last_path_42)

        # ======================
        # QUIT
        # ======================
        elif choice == "q":
            break

        else:
            print(center("Invalid choice"))
            time.sleep(0.5)
