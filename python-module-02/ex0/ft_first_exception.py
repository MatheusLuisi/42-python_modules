#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_first_exception.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/30 10:02:07 by mpinto-l            #+#    #+#            #
#   Updated: 2026/07/30 13:14:26 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def input_temperature(tmp_str: str) -> int:
    return int(tmp_str)


def test_temperature(user_input: str) -> None:
    print(f"\nInput data is '{user_input}'")
    try:
        tempertature = input_temperature(user_input)

    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    else:
        print(f'Temperature is now {tempertature}°C')


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    test_temperature('25')
    test_temperature('abc')
    print("\nAll tests completed - program didn't crash!")
