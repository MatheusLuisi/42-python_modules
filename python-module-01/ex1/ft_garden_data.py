#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 0                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_data.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/18 11:37:44 by mpinto-l            #+#    #+#            #
#   Updated: 2026/07/27 08:43:30 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:

    def __init__(self, name: str, height: float, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.days}days.")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower, 80, 45")
    cactus = Plant("Cactus", 15, 45)
    print("=== Garden Plant Registry ===")
    rose.show()
    sunflower.show()
    cactus.show()
