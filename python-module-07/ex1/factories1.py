#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   factories1.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/14 08:39:39 by mpinto-l            #+#    #+#            #
#   Updated: 2026/10/14 08:40:03 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex0.factories0 import CreatureFactory
from . import creatures1


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> creatures1.Sproutling:
        return creatures1.Sproutling()

    def create_evolved(self) -> creatures1.Bloomelle:
        return creatures1.Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> creatures1.Shiftling:
        return creatures1.Shiftling()

    def create_evolved(self) -> creatures1.Morphagon:
        return creatures1.Morphagon()
