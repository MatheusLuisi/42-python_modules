#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   factories0.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/14 08:39:26 by mpinto-l            #+#    #+#            #
#   Updated: 2026/10/14 08:39:31 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from abc import ABC, abstractmethod
from . import creatures0


class CreatureFactory(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def create_base(self) -> creatures0.Creature:
        ...

    @abstractmethod
    def create_evolved(self) -> creatures0.Creature:
        ...


class FlameFactory(CreatureFactory):
    def create_base(self) -> creatures0.Creature:
        return creatures0.Flameling()

    def create_evolved(self) -> creatures0.Creature:
        return creatures0.Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> creatures0.Creature:
        return creatures0.Aquabub()

    def create_evolved(self) -> creatures0.Creature:
        return creatures0.Torragon()
