#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   loading.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/14 11:10:25 by mpinto-l            #+#    #+#            #
#   Updated: 2026/10/14 16:40:51 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys
import importlib.metadata


def install_instructions() -> None:
    print("-------------------------------------------------------")
    print("Installig with pip: [pip install -r requirements.txt]\n")
    print("Installing with poetry: [poetry install]")
    print("poetry already detects the pyproject.toml file")
    print("-------------------------------------------------------\n")


def print_versions(pack: str, version: str) -> None:
    messages = {
        'pandas': " - Data manipulation ready",
        'numpy': " - Numerical computation ready",
        'requests': " - Network access ready",
        'matplotlib': " - Visualization ready"
    }
    print(f"\n[OK] {pack} ({version})", end='')

    if pack in messages:
        print(messages[pack])
    else:
        print()


def check_dependencies(packages: list[str]) -> bool:
    all_found = True

    for pack in packages:
        try:
            version = importlib.metadata.version(pack)
            print_versions(pack, version)
        except importlib.metadata.PackageNotFoundError:
            print(f"\n{pack} not found")
            install_instructions()
            all_found = False

    if not all_found:
        install_instructions()

    return all_found


def generate_data(quantity: int):
    import numpy as np


    rng: np.random.Generator = np.random.default_rng(seed=42)
    data_generate = rng.normal(loc=0, scale=1, size=quantity)
    return data_generate


def check_venv() -> bool:
    return sys.prefix != sys.base_prefix


def create_image(df) -> None:
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 6))
    plt.hist(df["values"], bins=30)
    plt.title("Matrix Data Analysis")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.savefig("matrix_analysis.png")
    plt.close()


def main() -> None:
    packages: list[str] = ['pandas', 'numpy', 'requests', 'matplotlib']

    print("LOADING STATUS: Loading programs...\n")

    if not check_venv():
        print("No Virtual enviroment detected")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env/Scripts/activate # On Windows\n")

    if not check_dependencies(packages):
        return

    else:
        print("Checking dependencies:\n")
        check_dependencies(packages)
        try:
            import pandas as pd # type: ignore[import-not-found]
            print("Analyzing Matrix data...")
            data_points = generate_data(1000)
            data_frame = pd.DataFrame({"values": data_points})

            print(f"Processing {len(data_frame)} data points")
            print("Generating visualization...")

            create_image(data_frame)

            print("Analysis complete!")
            print("Resultst saved to: matrix_analysis.png\n")

            print("Generating visualization...")

        except ImportError as error:
            print(error)


if __name__ == "__main__":
    main()
