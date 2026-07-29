#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_types.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/28 12:19:09 by mpinto-l            #+#    #+#            #
#   Updated: 2026/07/28 14:37:00 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


class Plant:

    def __init__(
            self,
            name: str,
            height: float,
            days: int,
            growth_rate: float = 1.0,
            ) -> None:
        self.name = name
        self._height = 0.0
        self._days = 0
        self.set_height(height)
        self.set_age(days)
        self.growth_rate = growth_rate

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = height
        print(f"Height updated: {height}cm")

    def get_height(self) -> float:
        return self._height

    def set_age(self, days: int) -> None:
        if days < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._days = days
        print(f"Age updated: {days}days")

    def get_age(self) -> int:
        return self._days

    def grow(self) -> None:
        self._height += self.growth_rate

    def age(self) -> None:
        self._days += 1

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._days} days old.")


class Flower(Plant):

    def __init__(
            self,
            name: str,
            height: float,
            days: int,
            color: str
            ) -> None:
        super().__init__(name, height, days)
        self.color = color
        self._bloom_status = False

    def bloom(self) -> None:
        self._bloom_status = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._bloom_status:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):

    def __init__(
            self,
            name: str,
            height: float,
            days: int,
            trunk_diameter: float,
            ) -> None:
        super().__init__(name, height, days)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of ", end='')
        print(f"{self._height:.1f}cm long and ", end='')
        print(f"{self.trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):

    def __init__(
            self,
            name: str,
            height: float,
            days: int,
            growth_rate: float,
            harvest_season: str,
            ) -> None:
        super().__init__(name, height, days, growth_rate)
        self.nutritional_value = 0
        self.harvest_season = harvest_season

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    rose.bloom()
    rose.show()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    oak.produce_shade()

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, 2.1, "April")
    tomato.show()
    for days in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()
