#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   generate.py                                          :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: zo-rakot <zo-rakot@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/23 01:04:03 by zo-rakot            #+#    #+#            #
#   Updated: 2026/06/25 06:14:18 by zo-rakot           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import random
import time

def clear():
    print("\033[H\033[J", end="")

def add_loops(maze, density=0.1):
    for y in range(maze.height):
        for x in range(maze.width):
            cell = maze.getCell(x, y)

            for direction, dx, dy in [
                ("N", 0, -1),
                ("S", 0, 1),
                ("E", 1, 0),
                ("W", -1, 0)
            ]:
                if random.random() < density:
                    nxt = maze.getCell(x + dx, y + dy)
                    if nxt:
                        # seulement si mur existe
                        if cell.coord[direction]:
                            maze.removeWall(cell, nxt, direction)

def generate(maze, delay=0.02, perfect=True):
    start = maze.getCell(0, 0)

    # reset visited
    maze.reset_visited()

    stack = []
    current = start
    current.visited = True

    try:
        while True:
            neighbors = maze.getNeighbors(current)

            if neighbors:
                direction, nxt = random.choice(neighbors)

                maze.removeWall(current, nxt, direction)

                stack.append(current)
                current = nxt
                current.visited = True

            elif stack:
                current = stack.pop()
            else:
                break

            clear()
            maze.display()
            time.sleep(delay)

    except KeyboardInterrupt:
        input("\rInterrupted, tap Enter to continu")

    # 🔥 IMPORTANT : ajouter les loops ici
    if not perfect:
        add_loops(maze, density=0.08)