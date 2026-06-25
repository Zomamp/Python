#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   maze.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: zo-rakot <zo-rakot@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/17 19:23:00 by zo-rakot            #+#    #+#            #
#   Updated: 2026/06/25 06:24:30 by zo-rakot           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


import time
import shutil

# ==========================
# Colors ANSI
# ==========================

THEMES = [
    {
        "WALL": "\033[38;5;99m",
        "PATH": "\033[38;5;51m",
        "START": "\033[38;5;46m",
        "END": "\033[38;5;196m"
    },
    {
        "WALL": "\033[38;5;208m",  # orange
        "PATH": "\033[38;5;226m",  # jaune
        "START": "\033[38;5;82m",  # vert
        "END": "\033[38;5;196m"
    },
    {
        "WALL": "\033[38;5;39m",   # bleu
        "PATH": "\033[38;5;201m",  # rose
        "START": "\033[38;5;46m",
        "END": "\033[38;5;196m"
    }
]

THEMES_42 = [
    {
        "WALL_42": "\033[38;5;99m",
        "PATH_42": "\033[38;5;51m",
        "START_42": "\033[38;5;46m",
        "END_42": "\033[38;5;196m"
    },
    {
        "WALL_42": "\033[38;5;208m",  # orange
        "PATH_42": "\033[38;5;226m",  # jaune
        "START_42": "\033[38;5;82m",  # vert
        "END_42": "\033[38;5;196m"
    },
    {
        "WALL_42": "\033[38;5;39m",   # bleu
        "PATH_42": "\033[38;5;201m",  # rose
        "START_42": "\033[38;5;46m",
        "END_42": "\033[38;5;196m"
    }
]

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
        self.theme_index = 0
        self.theme_index_42 = 0
        self.block_cells = self.carve_42()

    def createGrid(self) -> list[list[Cell]]:
        grid = []

        for y in range(self.height):
            row = []

            for x in range(self.width):
                row.append(Cell(x, y))
            grid.append(row)

        return (grid)

    def change_color(self):
        self.theme_index = (self.theme_index + 1) % len(THEMES)

    def change_color_42(self):
        self.theme_index_42 = (self.theme_index_42 + 1) % len(THEMES_42)

    def getCell(self, x: int, y: int) -> Cell | None:
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x]
        else:
            return None

    def reset_visited(self):
        for row in self.grid:
            for cell in row:
                cell.visited = False

    def getNeighbors(self, cell: Cell):
        x, y = cell.x, cell.y

        directions = [
            ("N", (x, y - 1)),
            ("S", (x, y + 1)),
            ("E", (x + 1, y)),
            ("W", (x - 1, y))
        ]

        neighbors = []

        for direction, (nx, ny) in directions:
            neighbor = self.getCell(nx, ny)

            if neighbor is None:
                continue

            if neighbor.visited:
                continue

            if neighbor in self.block_cells:
                continue

            neighbors.append((direction, neighbor))

        return neighbors

    def removeWall(self, current: Cell, nextCell: Cell, directions: str) -> None:
        if current in self.block_cells or nextCell in self.block_cells:
            return
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

    def get_padding(self, content_width: int) -> int:
        terminal_width = shutil.get_terminal_size().columns
        return max(0, (terminal_width - content_width) // 2)


    def print_title(self):
        theme = THEMES[self.theme_index]
        PATH = theme["PATH"]
        RESET = "\033[0m"

        title = [
            " █████╗ ███╗   ███╗ █████╗ ███████╗██╗███╗  ██╗██████╗     ██████╗  █████╗ ██████╗ ██╗   ██╗",
            "██╔══██╗████╗ ████║██╔══██╗╚══███╔╝██║████╗ ██║██╔════╝    ██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝",
            "███████║██╔████╔██║███████║  ███╔╝ ██║██╔██╗██║██║  ███╗   ██████╔╝███████║██████╔╝ ╚████╔╝ ",
            "██╔══██║██║╚██╔╝██║██╔══██║ ███╔╝  ██║██║╚████║██║   ██║   ██╔══██╗██╔══██║██╔══██╗  ╚██╔╝  ",
            "██║  ██║██║ ╚═╝ ██║██║  ██║███████║██║██║ ╚███║██║   ██║   ██████╔╝██║  ██║███████║   ██║   ",
            "╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚══╝╚█████╔╝    ╚═════╝ ╚═╝  ╚═╝╚═════╝   ╚═╝   ",
        ]

        title_width = max(len(line) for line in title)
        padding = self.get_padding(title_width)  # ✅ padding basé sur le titre

        for line in title:
            print(" " * padding + PATH + line + RESET)


    def clear():
        print("\033[H\033[J", end="")

    def display(self, path=None) -> None:
        theme = THEMES[self.theme_index]
        theme_42 = THEMES_42[self.theme_index_42] # Ajout de la couleur de 42 fa tsy nety leizy teo

        WALL = theme["WALL"]
        PATH = theme["PATH"]
        START = theme["START"]
        END = theme["END"]
        RESET = "\033[0m"

        PATH_42 = theme_42["PATH_42"]

        path_set = set(path) if path else set()

        maze_width = (self.width * 4) + 1
        padding = self.get_padding(maze_width)

        self.print_title()
        print(" " * padding + WALL + "╔" + "═══╦" * self.width + RESET)

        for y in range(self.height):
            line = WALL + "║" + RESET
            bottom = WALL + "╠" + RESET

            for x in range(self.width):
                cell = self.grid[y][x]

                if cell == self.start:
                    line += START + " 🤔" + RESET

                elif cell == self.end:
                    line += END + " 🏁" + RESET

                elif cell in self.block_cells:
                    line += PATH_42 + "███" + RESET

                elif cell in path_set:
                    line += PATH + " 🤪" + RESET

                else:
                    line += "   "

                # EAST wall
                if cell.coord["E"]:
                    line += WALL + "║" + RESET
                else:
                    line += " "

                # SOUTH wall
                if cell.coord["S"]:
                    bottom += WALL + "═══╩" + RESET
                else:
                    bottom += "   " + WALL + "╬" + RESET

            print(" " * padding + line)
            print(" " * padding + bottom)

    def carve_42(self):
        cx = self.width // 2
        cy = self.height // 2

        pattern = [
            # --- 4 ---
            (0, 0), (0, 1), (0, 2),
            (1, 2),
            (2, 0), (2, 1), (2, 2),
            (2, 3), (2, 4),

            # --- 2 ---
            (4, 0), (5, 0), (6, 0),
            (6, 1),
            (4, 2), (5, 2), (6, 2),
            (4, 3),
            (4, 4), (5, 4), (6, 4),
        ]

        ox = cx - 4
        oy = cy - 3

        cells = []
        for dx, dy in pattern:
            c = self.getCell(ox + dx, oy + dy)
            if c:
                cells.append(c)

        return set(cells)
