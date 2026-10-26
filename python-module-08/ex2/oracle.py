import os
import sys

try:
    from dotenv import load_dotenv, dotenv_values
except ImportError:
    print("python-dotenv not found")
    print("Install it with: pip install -r requirements.txt")
    sys.exit(1)


KEYS = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]


def load_config() -> dict[str, str | None]:
    load_dotenv(override=False)

    config: dict[str, str | None] = {}

    for key in KEYS:
        value = os.environ.get(key)
        config[key] = value

    return config


def validate_config(config: dict[str, str | None]) -> None:
    for key in KEYS:
        value = config[key]

        if not value:
            print(f"[WARNING] {key} is missing")

    mode = config["MATRIX_MODE"]

    if mode != "development" and mode != "production":
        print("[WARNING] MATRIX_MODE defaulting to development")
        config["MATRIX_MODE"] = "development"

    if not config["LOG_LEVEL"]:
        config["LOG_LEVEL"] = "INFO"

    print()


def print_config(config: dict[str, str | None]) -> None:
    mode = config["MATRIX_MODE"]

    print("Configuration loaded:")
    print(f"Mode: {mode}")

    database_url = config["DATABASE_URL"]

    if not database_url:
        print("Database: Not configured")
    elif mode == "development":
        print("Database: Connected to local instance")
    else:
        print("Database: Connected to production cluster")

    api_key = config["API_KEY"]

    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing key")

    log_level = config["LOG_LEVEL"]
    print(f"Log Level: {log_level}")

    zion_endpoint = config["ZION_ENDPOINT"]

    if not zion_endpoint:
        print("Zion Network: Offline")
    elif mode == "development":
        print(f"Zion Network: Online ({zion_endpoint})")
    else:
        print("Zion Network: Online (endpoint hidden)")

    print()


def has_hardcoded_secrets(
    config: dict[str, str | None]
) -> bool:
    try:
        with open(__file__, "r", encoding="utf-8") as file:
            source = file.read()
    except OSError:
        return False

    api_key = config["API_KEY"]
    database_url = config["DATABASE_URL"]

    if api_key and api_key in source:
        return True

    if database_url and database_url in source:
        return True

    return False


def env_in_gitignore() -> bool:
    try:
        with open(".gitignore", "r", encoding="utf-8") as file:
            lines = file.readlines()
    except OSError:
        return False

    for line in lines:
        line = line.strip()

        if line == ".env":
            return True

    return False


def active_overrides() -> list[str]:
    file_values = dotenv_values(".env")
    overrides: list[str] = []

    for key in KEYS:
        env_value = os.environ.get(key)

        if not env_value:
            continue

        if key not in file_values:
            continue

        file_value = file_values[key]

        if env_value != file_value:
            overrides.append(key)

    return overrides


def security_check(config: dict[str, str | None]) -> None:
    print("Environment security check:")

    if has_hardcoded_secrets(config):
        print("[WARNING] A configured value was found in the source code")
    else:
        print("[INFO] No current config value found in source")
        print("(basic check only)")

    if os.path.exists(".env"):
        if env_in_gitignore():
            print("[OK] .env file properly configured")
        else:
            print("[FAIL] .env is not in .gitignore")
    else:
        print("[WARNING] .env file not found (cp .env.example .env)")

    overrides = active_overrides()

    if overrides:
        print(
            "[OK] Environment overrides active: "
            + ", ".join(overrides)
        )
    else:
        print("[INFO] No environment overrides detected")

    print()


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")

    config = load_config()

    validate_config(config)
    print_config(config)
    security_check(config)

    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
