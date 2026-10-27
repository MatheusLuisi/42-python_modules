#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   oracle.py                                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/27 10:02:13 by mpinto-l            #+#    #+#            #
#   Updated: 2026/10/27 10:03:05 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import os
import sys

try:
    from dotenv import load_dotenv
except ImportError:
    print("Error: python-dotenv is not installed")
    print("Run: pip install -r requirements.txt")
    sys.exit(1)


def load_config() -> dict[str, str | None]:
    load_dotenv()

    config: dict[str, str | None] = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE", "development"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL", "INFO"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }

    return config


def check_config(config: dict[str, str | None]) -> bool:
    valid = True

    for key, value in config.items():
        if not value:
            print(f"[WARNING] {key} is missing")
            valid = False

    if config["MATRIX_MODE"] not in ("development", "production"):
        print("[WARNING] Invalid mode. Using development")
        config["MATRIX_MODE"] = "development"

    return valid


def print_config(config: dict[str, str | None]) -> None:
    mode = config["MATRIX_MODE"]

    print("\nConfiguration loaded:")
    print(f"Mode: {mode}")

    if config["DATABASE_URL"]:
        if mode == "development":
            print("Database: Local configuration loaded")
        else:
            print("Database: Production configuration loaded")
    else:
        print("Database: Not configured")

    if config["API_KEY"]:
        print("API Access: Key configured")
    else:
        print("API Access: Missing key")

    print(f"Log Level: {config['LOG_LEVEL']}")

    if config["ZION_ENDPOINT"]:
        print("Zion Network: Endpoint configured")
    else:
        print("Zion Network: Offline")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")

    if sys.prefix == sys.base_prefix:
        print("No virtual environment detected")
        print("Run: python3 -m venv .venv")
        print("Then activate it and install requirements.txt")
        return

    config = load_config()
    check_config(config)
    print_config(config)

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
