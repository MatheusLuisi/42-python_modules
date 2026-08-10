# Sometimes the built-in Python errors are not specific enough for your garden program.
# You can create your own error types to make your code clearer and more helpful.
# Create these simple custom exception classes:
# • GardenError - A basic error for garden problems
# • PlantError - For problems with plants (inherits from GardenError)
# • WaterError - For problems with watering (inherits from GardenError)
# Each custom exception should:
# • Be a simple class that inherits from Exception (or GardenError)
# • Have a specific default error message (e.g., “Unknown plant error”) if none is pro-
# vided

# Create functions that:
# • Raise your custom errors in different situations
# • Show how to catch your specific error types
# • Demonstrate that catching GardenError catches all garden-related errors

# $> python3 ft_custom_errors.py
# === Custom Garden Errors Demo ===
# Testing PlantError...
# Caught PlantError: The tomato plant is wilting!
# Testing WaterError...
# Caught WaterError: Not enough water in the tank!
# Testing catching all garden errors...
# Caught GardenError: The tomato plant is wilting!
# Caught GardenError: Not enough water in the tank!
# All custom error types work correctly!

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error"):
        super().__init__(message)


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as error:
        print(f"Caught PlantError: {error}")

    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as error:
        print(f"Caught WaterError: {error}")

    print("Testing catching all garden errors...")

    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as error:
        print(f"Caught GardenError: {error}")

    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as error:
        print(f"Caught GardenError: {error}")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
