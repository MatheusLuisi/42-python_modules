#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_transmutation_1.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/06 11:04:29 by mpinto-l            #+#    #+#            #
#   Updated: 2026/10/06 11:33:50 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import alchemy.transmutation as transmutation


def main() -> None:
    print("===Transmutation 1 ===")
    print("Import transmutation module directly")
    print(f"Testing lead to gold: {transmutation.lead_to_gold()}")


if __name__ == "__main__":
    main()
