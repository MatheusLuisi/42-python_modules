#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_alembic_0.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/05 11:41:40 by mpinto-l            #+#    #+#            #
#   Updated: 2026/10/05 12:14:37 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import elements


def main() -> None:
    print("=== Alembic 0 ===")
    print("Using 'import ...' structure to acess elements.py")
    print(f"Testing create_fire: {elements.create_fire()}")


if __name__ == "__main__":
    main()
