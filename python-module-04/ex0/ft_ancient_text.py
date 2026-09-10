#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_ancient_text.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/09/09 10:02:30 by mpinto-l            #+#    #+#            #
#   Updated: 2026/09/09 11:23:50 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print('Usage: ft_ancient_text.py <file>')
        return

    file_path = sys.argv[1]

    print('=== Cyber Archives Recovery ===')
    print(f"Accessing file '{file_path}'")

    try:
        file: typing.IO[str] = open(file_path, "r")
        content = file.read()

        print('---')
        print(content)
        print('---')

        file.close()
        print(f"File '{file_path}' closed.")

    except OSError as error:
        print(f"Error opening file '{file_path}': {error}")


if __name__ == "__main__":
    main()
