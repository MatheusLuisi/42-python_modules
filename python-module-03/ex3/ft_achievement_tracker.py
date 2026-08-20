#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_achievement_tracker.py                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/10 14:15:47 by mpinto-l            #+#    #+#            #
#   Updated: 2026/08/10 14:16:11 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import random


def gen_player_achievements(achievement_list: list[str]) -> set[str]:
    num_achievements = random.randint(0, 13)
    return set(random.sample(achievement_list, num_achievements))


def main() -> None:
    achievement_list = [
        'Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner',
        'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable',
        'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind',
        'Boss Slayer', 'Hidden Path Finder'
    ]

    alice = gen_player_achievements(achievement_list)
    bob = gen_player_achievements(achievement_list)
    charlie = gen_player_achievements(achievement_list)
    dylan = gen_player_achievements(achievement_list)

    players = (
        ("Alice", alice),
        ("Bob", bob),
        ("Charlie", charlie),
        ("Dylan", dylan)
    )

    print('=== Achievement Tracker System===\n')
    for name, achievements in players:
        print(f'Player {name}: {achievements}')

    all_distinct = alice.union(bob, charlie, dylan)
    print(f'\nAll distinct achievements: {all_distinct}\n')

    common = alice.intersection(bob, charlie, dylan)
    print(f'Common achievements: {common}\n')

    print(f'Only Alice has: {alice.difference(bob, charlie, dylan)}')
    print(f'Only Bob has: {bob.difference(alice, charlie, dylan)}')
    print(f'Only Charlie has: {charlie.difference(alice, bob, dylan)}')
    print(f'Only Dylan has: {dylan.difference(alice, bob, charlie)}\n')

    all_ach_set = set(achievement_list)
    for name, achievements in players:
        missing = all_ach_set.difference(achievements)
        print(f'{name} is missing: {missing}')


if __name__ == "__main__":
    main()
