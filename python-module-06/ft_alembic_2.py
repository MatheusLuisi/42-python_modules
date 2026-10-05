#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_alembic_2.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/05 11:41:51 by mpinto-l            #+#    #+#            #
#   Updated: 2026/10/05 12:28:28 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import alchemy.elements


def main() -> None:
    print("=== Alembic 2 ===")
    print("Accessing alchemy/elements.py using 'import ...' structure")
    print(f"Testing create_earth: {alchemy.elements.create_earth()}")


if __name__ == "__main__":
    main()
