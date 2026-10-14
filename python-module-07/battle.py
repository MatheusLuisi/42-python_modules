#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   battle.py                                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/14 08:39:42 by mpinto-l            #+#    #+#            #
#   Updated: 2026/10/14 08:40:01 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex0 import FlameFactory, AquaFactory


def main() -> None:
    flame_factory = FlameFactory()
    flameling = flame_factory.create_base()
    pyrodon = flame_factory.create_evolved()

    aqua_factory = AquaFactory()
    aquabub = aqua_factory.create_base()
    torragon = aqua_factory.create_evolved()

    print('Testing factory')
    print(flameling.describe())
    print(flameling.attack())
    print(pyrodon.describe())
    print(f"{pyrodon.attack()}\n")

    print('Testing factory')
    print(aquabub.describe())
    print(aquabub.attack())
    print(torragon.describe())
    print(f"{torragon.attack()}\n")

    print("Testing battle")
    print(flameling.describe())
    print("vs.")
    print(aquabub.describe())
    print("fight!")
    print(flameling.attack())
    print(aquabub.attack())


if __name__ == "__main__":
    main()
