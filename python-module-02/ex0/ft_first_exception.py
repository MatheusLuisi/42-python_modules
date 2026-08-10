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


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    for user_input in ("25", "abc"):
        print(f"\nInput data is '{user_input}'")
        try:
            temperature = input_temperature(user_input)
        except ValueError as error:
            print(f"Caught input_temperature error: {error}")
        else:
            print(f"Temperature is now {temperature}°C")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
