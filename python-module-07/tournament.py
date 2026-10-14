#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   tournament.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/14 08:39:47 by mpinto-l            #+#    #+#            #
#   Updated: 2026/10/14 08:39:57 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import List, Tuple
from ex0.creatures0 import Creature
from ex0.factories0 import (
    CreatureFactory,
    AquaFactory,
    FlameFactory,
)
from ex1.factories1 import (
    HealingCreatureFactory,
    TransformCreatureFactory,
)
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
)

Opponent = Tuple[CreatureFactory, BattleStrategy]


def battle(
        first: Creature,
        first_strategy: BattleStrategy,
        second: Creature,
        second_strategy: BattleStrategy,
        ) -> None:

    print("\n* Battle *")
    print(first.describe())
    print("vs.")
    print(second.describe())
    print("now fight!")

    if not first_strategy.is_valid(first):
        first_strategy.act(first)

    if not second_strategy.is_valid(second):
        second_strategy.act(second)

    first_strategy.act(first)
    second_strategy.act(second)


def tournament(opponents: List[Opponent]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    creatures = [
        (factory.create_base(), strategy)
        for factory, strategy in opponents
    ]

    try:
        for index, (creature_a, strategy_a) in enumerate(creatures):
            for creature_b, strategy_b in creatures[index + 1:]:
                battle(creature_a, strategy_a, creature_b, strategy_b,)
    except InvalidStrategyError as error:
        print(f"Battle error, aborting tournament: {error}")


def main() -> None:
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    flame = FlameFactory()
    aqua = AquaFactory()
    healing = HealingCreatureFactory()
    transforming = TransformCreatureFactory()

    print("Tournament 0 (basic)")
    tournament([
        (flame, normal),
        (healing, defensive),
    ])

    print("\nTournament 1 (error)")
    tournament([
        (flame, aggressive),
        (healing, defensive),
    ])

    print("\nTournament 2 (multiple)")
    tournament([
        (aqua, normal),
        (healing, defensive),
        (transforming, aggressive),
    ])


if __name__ == "__main__":
    main()
