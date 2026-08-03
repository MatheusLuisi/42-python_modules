#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_different_errors.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/30 15:24:10 by mpinto-l            #+#    #+#            #
#   Updated: 2026/07/30 15:36:48 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "abc" + 1  # mypy should flag this line as expected
    else:
        return


def test_error_types() -> None:
    for operation_number in range(5):
        print(f"Testing operation {operation_number}...")
        try:
            garden_operations(operation_number)
        except ValueError as default_message:
            print(f"Caught ValueError: {default_message}")
        except ZeroDivisionError as default_message:
            print(f"Caught ZeroDivisionError: {default_message}")
        except FileNotFoundError as default_message:
            print(f"Caught FileNotFoundError: {default_message}")
        except TypeError as default_message:
            print(f"Caught TypeError: {default_message}")
        else:
            print("Operation completed successfully")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("\nAll error types tested successfully!")
