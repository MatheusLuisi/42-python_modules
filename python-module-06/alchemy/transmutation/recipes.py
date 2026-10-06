#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   recipes.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/06 08:57:40 by mpinto-l            #+#    #+#            #
#   Updated: 2026/10/06 11:03:36 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from elements import create_fire
from ..potions import strength_potion
from ..elements import create_air


def lead_to_gold() -> str:
    return (
        f"Recipe transmuting Lead to Gold: brew {create_air()} and"
        f"{strength_potion()} mixed with {create_fire()}"
    )
