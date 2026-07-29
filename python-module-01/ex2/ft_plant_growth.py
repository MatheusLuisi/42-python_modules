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

    def __init__(
            self,
            name: str,
            height: float,
            days: int,
            rate: float = 1.0,
            ) -> None:
        self.name = name
        self.height = height
        self.days = days
        self.rate = rate

    def grow(self) -> None:
        self.height += self.rate

    def age(self) -> None:
        self.days += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.days}days.")


if __name__ == "__main__":
    rose = Plant("Rose", 25.0, 30, rate=0.8)
    print("=== Garden Plant Growth ===")
    rose.show()

    initial_height = rose.height
    for day in range(1, 8):
        rose.grow()
        rose.age()
        print(f"=== Day {day} ===")
        rose.show()

    total_growth = round(rose.height - initial_height, 1)
    print(f"Growth this week: {total_growth}cm")
