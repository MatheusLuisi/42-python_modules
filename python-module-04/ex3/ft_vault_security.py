#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_vault_security.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/09/10 10:08:29 by mpinto-l            #+#    #+#            #
#   Updated: 2026/09/10 10:59:52 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def secure_archive(
        file_path: str, mode: int = 0, to_write: str = ""
        ) -> tuple[bool, str]:
    if mode == 0:
        try:
            with open(file_path, "r") as file:
                return True, file.read()
        except OSError as error:
            return False, f"{error}"
    elif mode == 1:
        try:
            with open(file_path, "w") as file:
                file.write(to_write)
                return True, "'Content succesfully written to file'"
        except OSError as error:
            return False, f"{error}"
    else:
        return False, "No file provided"


def main() -> None:
    nonexistent_file = "not/existing/file"
    inaccessible_file = "/etc/shadow"
    regular_file = "test.txt"
    file_to_write = "test2.txt"

    print('=== Cyber Archives Security ===')

    print(
        "Using 'secure_archive' to read from a nonexistent file:\n"
        f"{secure_archive(nonexistent_file)}"
        )

    print(
        "Using 'secure_archive' to read from a inaccessible file:\n"
        f"{secure_archive(inaccessible_file)}"
        )

    print(
        "Using 'secure_archive' to read from a regular file:\n"
        f"{secure_archive(regular_file)}"
        )

    print(
        "Using 'secure_archive' to write previous content to a new file:\n"
        f"{secure_archive(file_to_write, 1, 'banana')}"
        )


if __name__ == "__main__":
    main()
