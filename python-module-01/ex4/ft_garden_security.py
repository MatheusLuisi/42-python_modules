#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_security.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/22 12:33:11 by mpinto-l            #+#    #+#            #
#   Updated: 2026/07/22 14:59:21 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


# ORIGINAL

# class Plant:

#     def __init__(self, name, height, lifetime):
#         self.name = name
#         self.height = height
#         self.lifetime = lifetime

#     def show(self):
#         print(f"{self.name}: {round(self.height, 1)}cm, {self.lifetime}days.")

#     def age(self):
#         self.lifetime += 1

#     def grow(self, rate):
#         self.height += rate

#     def grow_x_days(self, period, rate):
#         total_growth = round(period * rate, 1)
#         for days in range(1, period + 1):
#             self.grow(rate)
#             self.age()
#             print(f"=== Day {period} ===")
#             self.show()

#         return (total_growth)

# =============================


        # ensure plant height can not be negative
        # ensure plant age can not be negative
        # print error message from class when invalid values are provided
            # leaving data unchanged or creating the plant with default values
        # use encapsulation (not mangling)
        #create a system to validade data before storing it

# NEW

class Plant:

    def __init__(self, name: str, height: float, age: int):
        self._name = name
        self._height = None
        self._age = None


    def get_height(self):
        return self._height

    def validade_height(self, height):
        if not isinstance(height, float):
            self.set_height(0)
            print("Height update rejected")
        elif height < 0:
            print("Error, height can't be negative")
            print("Height update rejected")
        self.set_height(height)

    def set_height(self, height):
        self._height = height

    def get_age(self):
        return self._age

    def validade_age(self, age):
        if not isinstance(age, int):
            self.set_height(0)
            print("Age update rejected")
        elif age < 0:
            print("Error, age can't be negative")
            print("Age update rejected")
        self.set_age(age)

    def set_age(self, age):
        self._age = age

    def show(self):
        print(f"{self._name}: {round(self._height, 1)}cm, {self._age}days.")


    def age(self, age):
        if isinstance(self.validade_age(age)):
            print(f"Age updated: {self._age}days")

    def grow(self, rate):

    def grow_x_days(self, period, rate):





if __name__ == "__main__":
    rose = Plant("Rose", 25.0, 30)
