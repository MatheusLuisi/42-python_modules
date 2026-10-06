#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_kaboom_1.py                                       :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/06 13:03:28 by mpinto-l            #+#    #+#            #
#   Updated: 2026/10/06 13:11:24 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from alchemy.grimoire.dark_spellbook import dark_spell_record  # noqa: E402


def main() -> None:
    print("=== Kaboom 1 ===")
    print("Accesss to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")

    print(dark_spell_record("Forbidden", "Bats and arsenic"))


if __name__ == "__main__":
    main()
