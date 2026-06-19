#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   solver.py                                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: zo-rakot <zo-rakot@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/18 04:44:17 by zo-rakot            #+#    #+#            #
#   Updated: 2026/06/18 04:46:17 by zo-rakot           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import random

def solve(solving):
    solving.reset_visited()

    stack = []
    parent = {}

    current = solving.start
    current.visited = True

    while True:

        if current == solving.end:
            break

        neighbors = []
        x, y = current.x, current.y

        if not current.coord["N"]:
            n = solving.getCell(x, y - 1)
            if n and not n.visited:
                neighbors.append(n)

        if not current.coord["S"]:
            s = solving.getCell(x, y + 1)
            if s and not s.visited:
                neighbors.append(s)

        if not current.coord["E"]:
            e = solving.getCell(x + 1, y)
            if e and not e.visited:
                neighbors.append(e)

        if not current.coord["W"]:
            w = solving.getCell(x - 1, y)
            if w and not w.visited:
                neighbors.append(w)

        if neighbors:
            stack.append(current)
            next_cell = random.choice(neighbors)
            parent[next_cell] = current
            current = next_cell
            current.visited = True

        elif stack:
            current = stack.pop()

        else:
            return None

    # reconstruire chemin
    path = []
    while current in parent:
        path.append(current)
        current = parent[current]

    path.append(solving.start)
    return path[::-1] # liste[start:stop:step] -1 on avance a l'envers