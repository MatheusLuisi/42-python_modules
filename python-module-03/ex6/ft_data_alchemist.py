#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_data_alchemist.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/10 14:16:02 by mpinto-l            #+#    #+#            #
#   Updated: 2026/08/10 14:16:05 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

# Como no subject desse exercicio nao foi incluido explicitamente os metodos
# de dicionario (item() ou values() diferente do ex4) eu iterei diretamente
# pelo index do dicionario

import random


def main() -> None:
    print('=== Game Data Alchemist ===')

    initial_players = [
        'Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory',
        'john', 'kevin', 'Liam'
    ]

    print(f'Initial list of players: {initial_players}')

    all_capitalized = []
    for name in initial_players:
        all_capitalized.append(name.capitalize())
    print(f'New list with all names capiralized: {all_capitalized}')

    originally_capitalized = []
    for name in initial_players:
        if name[0].isupper():
            originally_capitalized.append(name)
    print(f'New list of captalized names only: {originally_capitalized}')

    score_dict = {}
    for name in all_capitalized:
        score_dict[name] = random.randint(1, 1000)
    print(f'\nScore dict: {score_dict}')

    total_score = 0
    for name in score_dict:
        total_score += score_dict[name]
    avg_score = total_score / len(score_dict)
    print(f'Score average is {round(avg_score, 2)}')

    high_scores = {}
    for name in score_dict:
        if score_dict[name] > avg_score:
            high_scores[name] = score_dict[name]
    print(f'\nHigh scores: {high_scores}')


if __name__ == "__main__":
    main()
