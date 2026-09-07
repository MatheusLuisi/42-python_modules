#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_data_stream.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/10 14:15:59 by mpinto-l            #+#    #+#            #
#   Updated: 2026/08/10 14:16:07 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ['alice', 'bob', 'charlie', 'dylan']
    actions = [
        'eat', 'run', 'sleep', 'grab', 'move', 'climb', 'swim', 'release',
        'use', 'jump'
        ]
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(
    events: list[tuple[str, str]]
    ) -> typing.Generator[tuple[str, str], None, None]:

    while len(events) > 0:
        index = random.randint(0, len(events) - 1)
        yield events.pop(index)


def main() -> None:
    print('=== Game Data Stream Processor ===')

    gen = gen_event()
    for i in range(1000):
        name, action = next(gen)
        print(f'Event {i}: Player {name} did action {action}')

    events_list = []
    for _ in range(10):
        events_list.append(next(gen))

    for event in consume_event(events_list):
        print(f'Got event from list: {event}')
        print(f'Remains in list: {events_list}')


if __name__ == "__main__":
    main()
