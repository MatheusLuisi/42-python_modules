#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_transmutation_0.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/06 09:21:45 by mpinto-l            #+#    #+#            #
#   Updated: 2026/10/06 11:05:00 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from alchemy.transmutation import recipes


def main() -> None:
    print("===Transmutation 0 ===")
    print("Using file alchemy/transmutation/recepies.py directly")
    print(f"Testing lead to gold: {recipes.lead_to_gold()}")


if __name__ == "__main__":
    main()
