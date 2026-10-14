#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   construct.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/14 08:39:11 by mpinto-l            #+#    #+#            #
#   Updated: 2026/10/14 10:59:55 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import os
import sys
import site


def check_python_version() -> str:
    return f"{sys.executable} - {sys.version[0:4]}"


def check_virtual_enviroment() -> str:
    return f"{os.path.basename(sys.prefix)}"


def matrix_status() -> bool:
    return sys.prefix != sys.base_prefix


def get_package_installation_path() -> str:
    for path in site.getsitepackages():
        if os.path.commonpath([sys.prefix, path]) == sys.prefix:
            return path
    return "Package path not found"


def inside_matrix_message() -> None:
    print("MATRIX STATUS: You're still plugged in\n")

    print(f"Current Python: {check_python_version()}")
    print("Virtual Enviroment: None detected\n")

    print("Warning: You're in the global environment!")
    print("The machines can see everything you install.\n")

    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env/Scripts/activate # On Windows\n")

    print("Then run this program again")


def outside_matrix_message() -> None:
    print("MATRIX STATUS: Welcome to the construct\n")

    print(f"Current Python: {check_python_version()}")
    print(f"Virtual Enviroment: {check_virtual_enviroment()}")
    print(f"Enviroment Path: {os.path.abspath(sys.prefix)}\n")

    print("SUCCESS: You're in an isolated enviroment!")
    print("Safe to install packages without affecting the global system.\n")

    print("Package installation path:")
    print(get_package_installation_path())


def main() -> None:
    if matrix_status():
        outside_matrix_message()
    else:
        inside_matrix_message()


if __name__ == "__main__":
    main()
