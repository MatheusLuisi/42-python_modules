#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_alembic_3.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/05 11:42:00 by mpinto-l            #+#    #+#            #
#   Updated: 2026/10/05 12:30:44 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from alchemy.elements import create_air


def main() -> None:
    print("=== Alembic 3 ===")
    print(
        "Accessing alchemy/elements.py using 'from ... import ...' structure"
        )
    print(f"Testing create_air: {create_air()}")


if __name__ == "__main__":
    main()
