#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_stream_management.py                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/09/09 11:18:57 by mpinto-l            #+#    #+#            #
#   Updated: 2026/09/10 11:16:53 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys
import typing


def get_user_input(message: str) -> str:
    print(message, end='')
    sys.stdout.flush()
    user_input = sys.stdin.readline().rstrip('\n')

    return user_input


def print_to_stderr(message: str) -> None:
    sys.stderr.write(f"[STDERR] {message}\n")


def main() -> None:
    if len(sys.argv) != 2:
        print('Usage: ft_stream_management.py <file>')
        return

    file_path = sys.argv[1]

    print('=== Cyber Archives Recovery & Preservation ===')
    print(f"Accessing file '{file_path}'")

    try:
        file: typing.IO[str] = open(file_path, "r")
        content = file.read()

        print('---')
        print(content)
        print('---')

        file.close()
        print(f"File '{file_path}' closed.\n")

        print("Transform data:")
        content = "\n".join(line + "#" for line in content.splitlines())
        print('---')
        print(content)
        print('---')

    except OSError as error:
        print_to_stderr(f"Error opening file '{file_path}': {error}")

    try:
        file_to_save = get_user_input("Enter new file name (or empty): ")
        if not file_to_save:
            print("Not saving data.")
        else:
            new_file: typing.IO[str] = open(file_to_save, "w")
            new_file.write(content)
            new_file.close()
            print(f"Saving data to '{file_to_save}'")
            print(f"Data saved in file '{file_to_save}'")

    except OSError as error:
        print_to_stderr(f"Error opening file '{file_to_save}': {error}")
        print("Data not saved.")


if __name__ == "__main__":
    main()
