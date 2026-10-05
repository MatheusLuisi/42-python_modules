#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_alembic_5.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/05 11:43:33 by mpinto-l            #+#    #+#            #
#   Updated: 2026/10/05 12:55:36 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from alchemy import create_air


def main() -> None:
    print("=== Alembic 5 ===")
    print("Accessing the alchemy module using 'from alchemy import ...'")
    print(f"Testing create air: {create_air()}")


if __name__ == "__main__":
    main()
