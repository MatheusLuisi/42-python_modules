#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   creatures0.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/14 08:39:21 by mpinto-l            #+#    #+#            #
#   Updated: 2026/10/14 08:39:29 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, creature_type: str) -> None:
        self.name = name
        self.creature_type = creature_type

    @abstractmethod
    def attack(self) -> str:
        ...

    def describe(self) -> str:
        return f"{self.name} is a {self.creature_type} type Creature"


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__(name="Flameling", creature_type="Fire")

    def attack(self) -> str:
        return 'Flameling uses Ember!'


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__(name="Pyrodon", creature_type="Fire/Flying")

    def attack(self) -> str:
        return 'Pyrodon uses Flamethrower!'


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__(name="Aquabub", creature_type="Water")

    def attack(self) -> str:
        return 'Aquabub uses Water Gun!'


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__(name="Torragon", creature_type="Water")

    def attack(self) -> str:
        return 'Torragon uses Hydro Pump!'
