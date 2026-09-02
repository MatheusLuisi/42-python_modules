#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_coordinate_system.py                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/10 14:15:44 by mpinto-l            #+#    #+#            #
#   Updated: 2026/09/02 12:46:59 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        try:
            user_input = input(
                "Enter new coordinates as floats in format 'x,y,z': "
                )
            positions = user_input.split(",")

            if len(positions) != 3:
                raise ValueError('Invalid Syntax')

            x = float(positions[0])
            y = float(positions[1])
            z = float(positions[2])

            return x, y, z

        except ValueError as error:
            if str(error) == "Invalid Syntax":
                print(f'{error}')
            else:
                parameter = str(error).split("'")[1]
                print(f"Error on parameter '{parameter}': {error}")


def calculate_distance(
        pos1: tuple[float, float, float],
        pos2: tuple[float, float, float]
        ) -> float:
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return round(distance, 4)


def main() -> None:
    center = 0.0, 0.0, 0.0

    print('=== Game Coordinate System ===\n')
    print('Get the first set of coodinates')

    x, y, z = get_player_pos()
    pos1 = x, y, z
    print(f'Got the first tuple: {pos1}')
    print(f'It includes: X={x}, Y={y}, Z={z}')
    print(f'Distance to center: {calculate_distance(center, pos1)}\n')

    print('Get a second set of coordinates')
    x, y, z = get_player_pos()
    pos2 = x, y, z
    distance = calculate_distance(pos1, pos2)
    print(f'Distance between the 2 sets of coordinates: {distance}')


if __name__ == "__main__":
    main()
