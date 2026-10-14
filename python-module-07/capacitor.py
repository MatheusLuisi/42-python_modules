#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   capacitor.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/14 08:39:44 by mpinto-l            #+#    #+#            #
#   Updated: 2026/10/14 08:39:59 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex1 import HealingCreatureFactory, TransformCreatureFactory


def main() -> None:
    healing_factory = HealingCreatureFactory()
    sproutling = healing_factory.create_base()
    bloomelle = healing_factory.create_evolved()

    transform_factory = TransformCreatureFactory()
    shiftling = transform_factory.create_base()
    morphagon = transform_factory.create_evolved()

    print("Testing Creature with healing capability")
    print("base:")
    print(sproutling.describe())
    print(sproutling.attack())
    print(sproutling.heal())

    print("\nevolved:")
    print(bloomelle.describe())
    print(bloomelle.attack())
    print(bloomelle.heal())

    print("\nTesting Creature with transform capability")
    print("base:")
    print(shiftling.describe())
    print(shiftling.attack())
    print(shiftling.transform())
    print(shiftling.attack())
    print(shiftling.revert())

    print("\nevolved:")
    print(morphagon.describe())
    print(morphagon.attack())
    print(morphagon.transform())
    print(morphagon.attack())
    print(morphagon.revert())


if __name__ == "__main__":
    main()
