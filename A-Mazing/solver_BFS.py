#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   solver_BFS.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: zo-rakot <zo-rakot@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/25 03:23:13 by zo-rakot            #+#    #+#            #
#   Updated: 2026/06/25 03:23:14 by zo-rakot           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from collections import deque
import time

def clear():
    print("\033[H\033[J", end="")


def solve_bfs(maze, delay=0.04):
    maze.reset_visited()

    queue = deque()
    parent = {}

    start = maze.start
    end = maze.end

    start.visited = True
    queue.append(start)

    try:
        while queue:
            clear()
            maze.display()
            time.sleep(delay)

            current = queue.popleft()

            if current == end:
                break

            x, y = current.x, current.y

            neighbors = []

            # Nord
            if not current.coord["N"]:
                n = maze.getCell(x, y - 1)
                if n and not n.visited:
                    neighbors.append(n)

            # Sud
            if not current.coord["S"]:
                s = maze.getCell(x, y + 1)
                if s and not s.visited:
                    neighbors.append(s)

            # Est
            if not current.coord["E"]:
                e = maze.getCell(x + 1, y)
                if e and not e.visited:
                    neighbors.append(e)

            # Ouest
            if not current.coord["W"]:
                w = maze.getCell(x - 1, y)
                if w and not w.visited:
                    neighbors.append(w)

            for nxt in neighbors:
                if not nxt.visited:
                    nxt.visited = True
                    parent[nxt] = current
                    queue.append(nxt)

        else:
            return None  # pas de solution

    except KeyboardInterrupt:
        input("\rYou Interrupt the program, tap Enter to continue")
        input("\rYou must regenerate the maze in the command to continue")

    # =========================
    # reconstruction du path
    # =========================
    path = []
    current = end

    if current not in parent and current != start:
        return None

    while current != start:
        path.append(current)
        current = parent[current]

    path.append(start)
    path.reverse()

    # =========================
    # animation finale
    # =========================
    for i in range(len(path)):
        clear()
        maze.display(path=path[:i + 1])
        time.sleep(delay)

    return path