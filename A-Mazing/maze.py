#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   maze.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: zo-rakot <zo-rakot@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/17 19:23:00 by zo-rakot            #+#    #+#            #
#   Updated: 2026/06/18 19:47:23 by zo-rakot           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import random

class Cell():
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.visited = False
        self.coord = {
            "N": True,
            "S": True,
            "E": True,
            "W": True
        }

    def markVisited(self) -> None:
        self.visited = True


class Maze():
    def __init__(self, width: int, height: int, entry: tuple[int, int], exiting: tuple[int, int]) -> None:
        self.width = width
        self.height = height

        self.grid = self.createGrid()
        self.stack = []
        self.current = None
        self.entry = entry
        self.exit = exiting
        self.start = self.getCell(entry[0], entry[1])
        self.end = self.getCell(exiting[0], exiting[1])

    def createGrid(self) -> list[list[Cell]]:
        grid = []

        for y in range(self.height):
            row = []

            for x in range(self.width):
                row.append(Cell(x, y))
            grid.append(row)

        return (grid)

    def getCell(self, x: int, y: int) -> Cell | None:
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x]
        else:
            return None

    def reset_visited(self):
        for row in self.grid:
            for cell in row:
                cell.visited = False

    def getNeighbors(self, cell: Cell) -> list[str, int]:
        x, y = cell.x, cell.y
        neighbors = []
        directions = [
            ("N", (x, y - 1)),
            ("S", (x, y + 1)),
            ("E", (x + 1, y)),
            ("W", (x - 1, y))
        ]

        for direction, (nx, ny) in directions:
            neighbor = self.getCell(nx, ny)

            if neighbor and not neighbor.visited:
                neighbors.append((direction, neighbor))

        return (neighbors)

    def removeWall(self, current: Cell, nextCell: Cell, directions: str) -> None:
        if directions == "N":
            current.coord["N"] = False
            nextCell.coord["S"] = False

        elif directions == "S":
            current.coord["S"] = False
            nextCell.coord["N"] = False

        elif directions == "E":
            current.coord["E"] = False
            nextCell.coord["W"] = False

        elif directions == "W":
            current.coord["W"] = False
            nextCell.coord["E"] = False

    def display(self, path=None) -> None:
        print("╋" + "━━━╋" * self.width)

        path_set = set(path) if path else set()
        for y in range(self.height):
            line = "▌"
            bottom = "╋"
            for x in range(self.width):
                cell = self.grid[y][x]

                if cell in path_set:
                    line += " ▒ "
                else:
                    line += "   "

                if cell.coord["E"]:
                    line += "▌"
                else:
                    line += " "

                if cell.coord["S"]:
                    bottom += "━━━╋"
                else:
                    bottom += "   ╋"
            print(line)
            print(bottom)
