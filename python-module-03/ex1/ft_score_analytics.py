#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_score_analytics.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/10 14:15:39 by mpinto-l            #+#    #+#            #
#   Updated: 2026/09/02 12:36:36 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


def main() -> None:
    print('=== Player Score Analytics ===')

    scores: list[int] = []
    for arg in sys.argv[1:]:
        try:
            score = int(arg)
            scores = scores + [score]
        except ValueError:
            print(f"Invalid parameter: '{arg}'")

    if not scores:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py "
            "<score1> <score2> ..."
        )
    else:
        print(f"Scores processed: {scores}")
        print(f'Total players: {len(scores)}')
        print(f'Total score: {sum(scores)}')
        print(f'Average score: {sum(scores) / len(scores)}')
        print(f'High score: {max(scores)}')
        print(f'Low score: {min(scores)}')
        print(f'Score range: {max(scores) - min(scores)}')


if __name__ == "__main__":
    main()
