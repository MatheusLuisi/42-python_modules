# 42 header



# expected output

# $> python3 ft_plant_types.py
# === Garden Plant Types ===
# === Flower
# Rose: 15.0cm, 10 days old
# Color: red
# Rose has not bloomed yet
# [asking the rose to bloom]
# Rose: 15.0cm, 10 days old
# Color: red
# Rose is blooming beautifully!
# === Tree
# Oak: 200.0cm, 365 days old
# Trunk diameter: 5.0cm
# [asking the oak to produce shade]
# Tree Oak now produces a shade of 200.0cm long and 5.0cm wide.
# === Vegetable
# Tomato: 5.0cm, 10 days old
# Harvest season: April
# Nutritional value: 0
# [make tomato grow and age for 20 days]
# Tomato: 47.0cm, 30 days old
# Harvest season: April
# Nutritional value: 20




class Plant:

    def __init__(self, name: str, height: float, days: int, rate: float = 1.0):
        self.name = name
        self._height = 0.0
        self._days = 0
        self.set_height(height)
        self.set_age(days)
        self.rate = rate

    def set_height(self, height) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = height
        print(f"Height updated: {height}cm")

    def get_height(self) -> float:
        return self._height

    def set_age(self, days) -> None:
        if days < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._days = days
        print(f"Age updated: {days}days")

    def get_age(self) -> int:
        return self._days

    def grow(self) -> None:
        self.height += self.rate

    def age(self) -> None:
        self.days += 1

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._days} days old.")

class Flower(Plant):

    def __init__(self, name: str, height: float, days: int, color: str):
        super().__init__(name, height, days)
        self.color = color
        self._bloom_status = False

    def bloom(self) -> None:
        self._has_bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._has_bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")

class Tree(Plant):

    def __init__(self, name: str, height: float, days: int, diameter: float):
        super().__init__(name, height, days)
        self.diameter = diameter

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of", end='')
        print(f"{self._height} long and {self.diameter} wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.diameter:1f}cm")



if __name__ == "__main__":
