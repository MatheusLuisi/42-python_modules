#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   loading.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/14 11:10:25 by mpinto-l            #+#    #+#            #
#   Updated: 2026/10/14 11:34:23 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys
import importlib


def install_instructions() -> None:
    print("-------------------------------------------------------")
    print("Installig with pip: [pip install -r requirements.txt]\n")
    print("Installing with poetry: [poetry install]")
    print("poetry already detects the pyproject.toml file")
    print("-------------------------------------------------------\n")


def check_dependencies() -> None:
    return


def generate_data() -> None:
    return


def create_image() -> None:
    return


def main() -> None:
    install_instructions()


if __name__ == "__main__":
    main()
