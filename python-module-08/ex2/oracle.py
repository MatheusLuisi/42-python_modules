#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   oracle.py                                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/27 10:02:13 by mpinto-l            #+#    #+#            #
#   Updated: 2026/10/28 15:02:08 by mpinto-l           ###   ########.fr      #
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
        valid = False

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

    zion_endpoint = config["ZION_ENDPOINT"]

    if not zion_endpoint:
        print("Zion Network: Offline")
    elif mode == "development":
        print(f"Zion Network: Online ({zion_endpoint})")
    else:
        print("Zion Network: Online (endpoint hidden)")


def has_hardcoded_secrets(config: dict[str, str | None]) -> bool:
    try:
        with open(__file__, "r", encoding="utf-8") as file:
            source = file.read()
    except OSError:
        return False

    for key in ("API_KEY", "DATABASE_URL"):
        value = config[key]

        if value and value in source:
            return True

    return False


def env_in_gitignore() -> bool:
    try:
        with open(".gitignore", "r", encoding="utf-8") as file:
            lines = []

            for line in file:
                line = line.strip()
                lines.append(line)

    except OSError:
        return False

    for line in lines:
        if line == ".env":
            return True

    return False


def security_check(config: dict[str, str | None]) -> None:
    print("\nEnvironment security check:")

    if has_hardcoded_secrets(config):
        print("[WARNING] A config value was found in the source code")
    else:
        print("[OK] No config value found in the source code")

    if not os.path.exists(".env"):
        print("[WARNING] .env file not found (cp .env.example .env)")
    elif env_in_gitignore():
        print("[OK] .env file properly configured")
    else:
        print("[FAIL] .env is not in .gitignore")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")

    config = load_config()
    valid = check_config(config)

    print_config(config)
    security_check(config)

    if not valid:
        print("\n[WARNING] Some configurations need attention.")
        return

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
