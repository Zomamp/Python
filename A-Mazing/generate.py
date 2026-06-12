#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   generate.py                                          :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: zo-rakot <zo-rakot@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/12 02:02:49 by zo-rakot            #+#    #+#            #
#   Updated: 2026/06/12 02:06:27 by zo-rakot           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def generate_maze(grille: list, length: int, height: int) -> None:
    """Generation of the maze"""
    oppose = {
        "North" : "South",
        "South" : "North",
        "East" : "West",
        "West" : "East"
    }

    voisins = [
        ("North", 0, -1),
        ("South", 0, 1),
        ("East", 1, 0),
        ("West", -1, 0)
    ]