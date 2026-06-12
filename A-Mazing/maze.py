#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   maze.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: zo-rakot <zo-rakot@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/12 00:59:56 by zo-rakot            #+#    #+#            #
#   Updated: 2026/06/12 01:27:44 by zo-rakot           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def create_grille(length: int, height: int) -> list:
    grille = []

    for y in range(height):
        line = []
        for x in range(length):
            cellule = {
                "North" : True,
                "South" : True,
                "East" : True,
                "West" : True,
                "Visited" : False
            }
            line.append(cellule)
        grille.append(line)
    return (grille)
