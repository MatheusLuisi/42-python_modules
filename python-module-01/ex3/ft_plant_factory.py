#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_factory.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/21 12:27:32 by mpinto-l            #+#    #+#            #
#   Updated: 2026/07/22 12:25:46 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:

    def __init__(self, name, height, lifetime):
        self.name = name
        self.height = height
        self.lifetime = lifetime

    def show(self):
        print(f"{self.name}: {round(self.height, 1)}cm, {self.lifetime}days.")

    def age(self):
        self.lifetime += 1

    def grow(self, rate):
        self.height += rate

    def grow_x_days(self, period, rate):
        total_growth = round(period * rate, 1)
        for period in range(1, period + 1):
            self.grow(rate)
            self.age()
            print(f"=== Day {period} ===")
            self.show()

        return (total_growth)


if __name__ == "__main__":
    print("=== Plant Factory Output")
    plants = [
                Plant("Rose", 25.0, 30),
                Plant("Oak", 200.0, 365),
                Plant("Cactus", 5.0, 90),
                Plant("Sunflower", 80.0, 45),
                Plant("Fern", 15.0, 120),
                ]

for x in plants:
    print("Created: ", end='')
    x.show()
