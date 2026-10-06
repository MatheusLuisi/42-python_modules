#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   potions.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/05 14:43:57 by mpinto-l            #+#    #+#            #
#   Updated: 2026/10/06 08:51:35 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from elements import create_fire, create_water

from .elements import create_air, create_earth


def healing_potion() -> str:
    return (
        f"Healing potion brewed with '{create_earth()}' and '{create_air()}'"
    )


def strength_potion() -> str:
    return (
        f"Strength potion brewed with '{create_fire()}' and '{create_water()}'"
    )
