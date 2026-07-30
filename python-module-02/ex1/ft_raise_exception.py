#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_raise_exception.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/30 11:08:10 by mpinto-l            #+#    #+#            #
#   Updated: 2026/07/30 14:50:23 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def input_temperature(tmp_str: str) -> int:
    tmp = int(tmp_str)
    if tmp < 0:
        raise ValueError(f"{tmp}°C is too cold for the plants (min 0°C)")
    if tmp > 40:
        raise ValueError(f"{tmp}°C is too hot for the plants (max 40°C)")
    else:
        return tmp


def test_temperature(user_input: str) -> None:
    print(f"\nInput data is '{user_input}'")
    try:
        tmp = input_temperature(user_input)

    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    else:
        print(f'Temperature is now {tmp}°C')


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    test_temperature('25')
    test_temperature('abc')
    test_temperature('120')
    test_temperature('-42')
    print("\nAll tests completed - program didn't crash!")
