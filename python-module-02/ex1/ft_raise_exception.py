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
    temp = int(tmp_str)
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    return temp


def test_temperature() -> None:
    for user_input in ("25", "abc", "100", "-50"):
        print(f"\nInput data is '{user_input}'")
        try:
            temp = input_temperature(user_input)
        except ValueError as error_message:
            print(f"Caught input_temperature error: {error_message}")
        else:
            print(f"Temperature is now {temp}°C")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    test_temperature()
    print("\nAll tests completed - program didn't crash!")
