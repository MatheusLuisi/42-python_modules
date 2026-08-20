#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_score_analytics.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/10 14:15:39 by mpinto-l            #+#    #+#            #
#   Updated: 2026/08/10 15:27:37 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


def main() -> None:
    print("=== Player Score Analytics ===")

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
        total = sum(scores)
        average = total / len(scores)
        high_score = max(scores)
        low_score = min(scores)
        score_range = high_score - low_score

        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {total}")
        print(f"Average score: {average}")
        print(f"High score: {high_score}")
        print(f"Low score: {low_score}")
        print(f"Score range: {score_range}")


if __name__ == "__main__":
    main()
