#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_alembic_1.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/05 11:41:45 by mpinto-l            #+#    #+#            #
#   Updated: 2026/10/05 12:26:58 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from elements import create_water


def main() -> None:
    print("=== Alembic 1 ===")
    print("Using 'from ... import ...' structure to access elementy.py")
    print(f"Testing create_water: {create_water()}")


if __name__ == "__main__":
    main()
