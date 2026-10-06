#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_kaboom_0.py                                       :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/06 12:42:23 by mpinto-l            #+#    #+#            #
#   Updated: 2026/10/06 12:49:11 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import alchemy.grimoire as grimoire


def main() -> None:
    spell = grimoire.light_spell_record("Fantasy", "Earth, wind, fire")
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    print(f"Testing record light spell: {spell}")


if __name__ == "__main__":
    main()
