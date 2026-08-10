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
    print("=== Garden Error Types Demo ===")
    for operation_number in range(5):
        print(f"Testing operation {operation_number}...")
        try:
            garden_operations(operation_number)
        except ValueError as error:
            print(f"Caught ValueError: {error}")
        except ZeroDivisionError as error:
            print(f"Caught ZeroDivisionError: {error}")S
        except FileNotFoundError as error:
            print(f"Caught FileNotFoundError: {error}")
        except TypeError as error:
            print(f"Caught TypeError: {error}")
        else:
            print("Operation completed successfully")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
