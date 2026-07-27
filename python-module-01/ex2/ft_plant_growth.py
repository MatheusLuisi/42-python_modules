#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_growth.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/21 09:11:29 by mpinto-l            #+#    #+#            #
#   Updated: 2026/07/27 12:31:02 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:

    def __init__(self, name: str, height: float, lifetime: int):
        self.name = name
        self.height = height
        self.lifetime = lifetime

    def grow(self, rate: float):
        self.height += rate

    def age(self):
        self.lifetime += 1

    def show(self):
        print(f"{self.name}: {round(self.height, 1)}cm, {self.lifetime}days.")

    def grow_x_days(self, period: int, rate: float):
        total_growth = round(period * rate, 1)
        for period in range(1, period + 1):
            self.grow(rate)
            self.age()
            print(f"=== Day {period} ===")
            self.show()

        return (round(total_growth, 1))


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25.0, 30)
    rose.grow_x_days(7, 0.8)
    print(f"Growth this week: {rose.grow_x_days(7, 0.8)}")
