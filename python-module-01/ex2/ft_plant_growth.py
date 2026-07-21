#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_growth.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/21 09:11:29 by mpinto-l            #+#    #+#            #
#   Updated: 2026/07/21 12:40:57 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self, rate):
        self.height += rate

    def agee(self):
        self.age += 1

    def show(self):
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age}days.")


def ft_plant_growth(days, name, height, age, rate):
    input = Plant(name, height, age)
    total_growth = round(days * rate, 1)
    print("=== Garden Plant Growth ===")
    for days in range(1, days + 1):
        input.grow(rate)
        input.agee()
        print(f"=== Day {days} ===")
        input.show()
    print(f"Growth this week: {total_growth}")


if __name__ == "__main__":
    ft_plant_growth(7, "Rose", 25.0, 30, 0.8)
