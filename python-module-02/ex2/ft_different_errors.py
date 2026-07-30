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
        raise ValueError

    if operation_number == 1:
        raise ZeroDivisionError

    if operation_number == 2:
        raise FileNotFoundError

    if operation_number == 3:
        raise TypeError


def test_error_types(operation_number: int) -> None:
    try:
        garden_operations(operation_number)

    except




if __name__ == "__main__":
