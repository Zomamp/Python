#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_coordinate_system.py                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: zo-rakot <zo-rakot@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/06 20:24:49 by zo-rakot            #+#    #+#            #
#   Updated: 2026/06/06 20:25:30 by zo-rakot           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


import math


def demand_looping() -> tuple[float, float, float]:
    while True:
        try:
            coord_00 = input(
                "Enter new coordinates as floats in format 'x,y,z': "
            ).split(",")
            helping = []
            for values in coord_00:
                helping += [float(values)]
            if len(helping) != 3:
                raise ValueError("Invalid syntax")

            return (helping[0], helping[1], helping[2])
        except ValueError:
            print("Invalid syntax")


def demand_looping_01() -> tuple[float, float, float]:
    while True:
        try:
            coord_01 = input(
                "Enter new coordinates as floats in format 'x,y,z': "
            ).split(",")
            helping_01 = []
            for values_01 in coord_01:
                helping_01 += [float(values_01)]
            if len(helping_01) != 3:
                raise ValueError("Invalid syntax")

            return (helping_01[0], helping_01[1], helping_01[2])

        except ValueError as e:
            print(f"Error on parameter '{values_01}', {e}")


def get_player_pos() -> float:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    first_sight = demand_looping()
    print(f"Got a first tuple: {first_sight}")
    x1 = first_sight[0]
    y1 = first_sight[1]
    z1 = first_sight[2]
    print(
        f"It includes: X={first_sight[0]},"
        f" Y={first_sight[1], }"
        f" Z={first_sight[2]}"
        )
    distance_1 = math.sqrt((x1**2) + (y1**2) + (z1**2))
    Round = round(distance_1, 4)
    print(f"Distance to center: {Round}")

    print("Get a second set of coordinates")
    second_sight = demand_looping_01()
    x2 = second_sight[0]
    y2 = second_sight[1]
    z2 = second_sight[2]
    formul_final = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(
        f"Distance between the 2 sets of coordinates:"
        f" {round(formul_final, 4)}"
        )
    return (formul_final)


if __name__ == "__main__":
    get_player_pos()
