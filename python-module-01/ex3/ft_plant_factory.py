#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_factory.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/21 12:27:32 by mpinto-l            #+#    #+#            #
#   Updated: 2026/07/21 12:43:27 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:

    def __init__(self, name, height, age):
        self.name = name
        self.height = round(height, 1)
        self.age = age

    def show(self):
        print(f"Created {self.name}: {self.height}cm, {self.age} days old")


def ft_plant_factory(name: str, height: float, age: int):
    input = Plant(name, height, age)
    input.show()


if __name__ == "__main__":
    ft_plant_factory("Rose", 25.0, 30)
    ft_plant_factory("Oak", 200.0, 365)
    ft_plant_factory("Cactus", 5.0, 90)
    ft_plant_factory("Sunflower", 80.0, 45)
    ft_plant_factory("Fern", 15.0, 120)
