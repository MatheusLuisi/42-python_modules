#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_coordinate_system.py                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/10 14:15:44 by mpinto-l            #+#    #+#            #
#   Updated: 2026/08/10 14:16:13 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

# $> python3 ft_coordinate_system.py
# === Game Coordinate System ===
# Get a first set of coordinates
# Enter new coordinates as floats in format 'x,y,z': hello world
# Invalid syntax
# Enter new coordinates as floats in format 'x,y,z': 1.0 , 2.5, 3.0
# Got a first tuple: (1.0, 2.5, 3.0)
# It includes: X=1.0, Y=2.5, Z=3.0
# Distance to center: 4.0311
# Get a second set of coordinates
# Enter new coordinates as floats in format 'x,y,z': 4,abc,5
# Error on parameter 'abc': could not convert string to float: 'abc'
# Enter new coordinates as floats in format 'x,y,z': 4,5,6
# Distance between the 2 sets of coordinates: 4.9244

import math


def get_player_pos() -> tuple[float, float, float]:
    prompt = "Enter new coordinates as floats in format 'x,y,z': "

    while True:
        user_input = input(prompt)
        coordinates = user_input.split(',')

        try:
            x_str, y_str, z_str = coordinates
        except ValueError:
            print('Invalid syntax')
            continue

        try:
            x = float(x_str)
        except ValueError as e:
            print(f"Error on parameter '{x_str}': {e}")
            continue

        try:
            y = float(y_str)
        except ValueError as e:
            print(f"Error on parameter '{y_str}': {e}")
            continue

        try:
            z = float(z_str)
        except ValueError as e:
            print(f"Error on parameter '{z_str}': {e}")
            continue

        return (x, y, z)


def calculate_distance(
    p1: tuple[float, float, float], p2: tuple[float, float, float]
) -> float:
    return math.sqrt(
        (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2 + (p2[2] - p1[2]) ** 2
        )


def main() -> None:
    print('=== Game Coordinate System ===\n')
    print('Get a first set of coordinates')
    pos1 = get_player_pos()
    print(f'Got a first tuple: {pos1}')
    print(f'It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}')

    center = (0.0, 0.0, 0.0)
    dist1 = calculate_distance(pos1, center)
    print(f'Distance to center: {round(dist1, 4)}')

    print('Get a second set of coodinates')
    pos2 = get_player_pos()
    dist2 = calculate_distance(pos1, pos2)
    print(f'Distance between the 2 sets of coordinates: {round(dist2, 4)}')


if __name__ == "__main__":
    main()
