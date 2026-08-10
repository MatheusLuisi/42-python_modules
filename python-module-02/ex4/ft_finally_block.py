# Your garden program needs to clean up resources, even if an error has occurred. The
# finally block is perfect for this - it always runs, whether there was an error or not.
# Write a function water_plant(plant_name) that:
# • Tries to water the plant
# • Succeeds if the plant name is capitalized
# • Raises an error if the plant name is not capitalized (use your PlantError exception
# from the previous exercise)
# • Prints a message on success
# Create a test_watering_system() function that:
# • Opens the watering system (just print a message)
# • Waters several plants using water_plant()
# • Uses try/except/finally structure
# • Handles errors if a plant name is invalid and can’t be watered. In that case, stop
# the test and immediately return to main.
# • Always closes the watering system in a finally block
# • Shows that cleanup always happens, even when there’s an error


# $> python3 ft_finally_block.py
# === Garden Watering System ===
# Testing valid plants...
# Opening watering system
# Watering Tomato: [OK]
# Watering Lettuce: [OK]
# Watering Carrots: [OK]
# Closing watering system
# Testing invalid plants...
# Opening watering system
# Watering Tomato: [OK]
# Caught PlantError: Invalid plant name to water: 'lettuce'
# .. ending tests and returning to main
# Closing watering system
# Cleanup always happens, even with errors!

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(
            f"Invalid plant name to water: '{plant_name}'"
        )

    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")

    print("Testing valid plants...")
    print("Opening watering system")

    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as error:
        print(f"Caught PlantError: {error}")
    finally:
        print("Closing watering system")

    print("Testing invalid plants...")
    print("Opening watering system")

    try:
        water_plant("Tomato")
        water_plant("lettuce")
        water_plant("Carrots")
    except PlantError as error:
        print(f"Caught PlantError: {error}")
    finally:
        print("Closing watering system")

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
