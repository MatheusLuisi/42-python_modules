#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_distillation_0.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/06 08:40:42 by mpinto-l            #+#    #+#            #
#   Updated: 2026/10/06 08:55:20 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from alchemy import potions


def main() -> None:
    print("=== Distilation 0 ===")
    print("Direct access to alchemy/potions.py")
    print(f"Testing strength_potion: {potions.strength_potion()}")
    print(f"Testing healing_potion: {potions.healing_potion()}")


if __name__ == "__main__":
    main()
