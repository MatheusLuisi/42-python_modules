#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   loading.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/14 11:10:25 by mpinto-l            #+#    #+#            #
#   Updated: 2026/10/27 09:45:55 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys
import importlib.metadata
from typing import Any


def install_instructions() -> None:
    print("-------------------------------------------------------")
    print("Installing with pip: [pip install -r requirements.txt]\n")
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
            print(f"\n[MISSING] {pack} not found")
            all_found = False

    print()
    if not all_found:
        install_instructions()

    return all_found


def show_pip_x_poetry() -> None:
    print("Dependency management:")
    print(" - pip uses requirements.txt")
    print("   Install with: pip install -r requirements.txt")
    print(" - Poetry uses pyproject.toml")
    print("   Install with: poetry install")
    print(" - Both manage project dependencies")
    print(f" - Python prefix: {sys.prefix}\n")


def generate_data(quantity: int) -> Any:
    np = importlib.import_module("numpy")

    rng = np.random.default_rng(seed=42)
    return rng.normal(loc=0, scale=1, size=quantity)


def check_venv() -> bool:
    return sys.prefix != sys.base_prefix


def create_image(df: Any) -> None:
    plt = importlib.import_module("matplotlib.pyplot")

    plt.figure(figsize=(10, 6))
    plt.hist(df["values"], bins=30)
    plt.title("Matrix Data Analysis")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.savefig("matrix_analysis.png")
    plt.close()


def main() -> None:
    packages: list[str] = ['pandas', 'numpy', 'matplotlib']

    print("LOADING STATUS: Loading programs...\n")

    if not check_venv():
        print("No Virtual enviroment detected")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env/Scripts/activate # On Windows\n")

    if not check_dependencies(packages):
        return

    show_pip_x_poetry()

    try:
        pd = importlib.import_module("pandas")

        print("Analyzing Matrix data...")
        data_points = generate_data(1000)
        data_frame = pd.DataFrame({"values": data_points})

        print(f"Processing {len(data_frame)} data points...")
        print("Generating visualization...")

        create_image(data_frame)

        print("\nAnalysis complete!")
        print("Results saved to: matrix_analysis.png")

    except ImportError as error:
        print("[ERROR] A required package could not be imported.")
        print(f"Details: {error}")
        print("Check your dependencies and install them again.")


if __name__ == "__main__":
    main()
