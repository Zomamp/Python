#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   generate.py                                          :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: zo-rakot <zo-rakot@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/12 02:02:49 by zo-rakot            #+#    #+#            #
#   Updated: 2026/06/18 04:53:39 by zo-rakot           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import random
from maze import Maze


def generate(maze: Maze) -> None:
    current = maze.getCell(0, 0)
    current.visited = True
    stack = []

    while True:
        neighbors = maze.getNeighbors(current)

        if neighbors:
            direction, next_cell = random.choice(neighbors)

            maze.removeWall(current, next_cell, direction)

            stack.append(current)

            current = next_cell
            current.visited = True

        elif stack:
            current = stack.pop()

        else:
            break
