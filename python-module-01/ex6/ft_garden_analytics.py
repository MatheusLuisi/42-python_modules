class Plant:

    def __init__(
            self,
            name: str,
            height: float,
            days: int,
            growth_rate: float = 1.0,
            ):
        self.name = name
        self._height = 0.0
        self._days = 0
        self.set_height(height)
        self.set_age(days)
        self.growth_rate = growth_rate

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
        self._height += self.growth_rate

    def age(self) -> None:
        self._days += 1

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._days} days old.")


class Flower(Plant):

    def __init__(self, name: str, height: float, days: int, color: str):
        super().__init__(name, height, days)
        self.color = color
        self._bloom_status = False

    def bloom(self) -> None:
        self._bloom_status = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._bloom_status:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Seed(Flower):
    pass


class Tree(Plant):

    def __init__(self, name: str, height: float, days: int, diameter: float):
        super().__init__(name, height, days)
        self.diameter = diameter

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of ", end='')
        print(f"{self._height}cm long and {self.diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.diameter:.1f}cm")


class Vegetable(Plant):

    def __init__(
            self,
            name: str,
            height: float,
            days: int,
            growth_rate: float,
            harvest_season: str,
            ):
        super().__init__(name, height, days, growth_rate)
        self.nutrients_value = 0
        self.harvest_season = harvest_season

    def age_and_grow(self, period: int) -> None:
        for days in range(1, period + 1):
            super().grow()
            super().age()
            self.nutrients_value += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutricional value: {self.nutrients_value}")


class Anonymous(Plant):
    pass


if __name__ == "__main__":
    print("=== Garden statistics ===")
