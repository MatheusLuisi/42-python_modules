class Plant:

    def __init__(
            self,
            name: str,
            height: float,
            days: int,
            growth_rate: float = 1.0,
            ) -> None:
        self.name = name
        self._height = 0.0
        self._days = 0
        self.set_height(height)
        self.set_age(days)
        self.growth_rate = growth_rate
        self._stats = Plant.Stats()

    @staticmethod
    def year_old(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    class Stats:

        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def increment_grow(self) -> None:
            self._grow_count += 1

        def increment_age(self) -> None:
            self._age_count += 1

        def increment_show(self) -> None:
            self._show_count += 1

        def show_stats(self, name: str) -> None:
            print(f"[statistics for {name}]")
            print(f"Stats: {self._grow_count} grow, ", end='')
            print(f"{self._age_count} age, {self._show_count} show")

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = height
        print(f"Height updated: {height}cm")

    def get_height(self) -> float:
        return self._height

    def set_age(self, days: int) -> None:
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
        self._stats.increment_grow()

    def age(self, days: int = 1) -> None:
        self._days += days
        self._stats.increment_age()

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._days} days old.")
        self._stats.increment_show()


class Flower(Plant):

    def __init__(
            self,
            name: str,
            height: float,
            days: int,
            color: str,
            growth_rate: float,
            ) -> None:
        super().__init__(name, height, days, growth_rate)
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

    def __init__(
            self,
            name: str,
            height: float,
            days: int,
            color: str,
            growth_rate: float,
            ) -> None:
        super().__init__(name, height, days, color, growth_rate)
        self.seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")


class Tree(Plant):

    def __init__(
            self,
            name: str,
            height: float,
            days: int,
            trunk_diameter: float,
            ) -> None:
        super().__init__(name, height, days)
        self.trunk_diameter = trunk_diameter
        self._stats: Tree.Stats = Tree.Stats()

    class Stats(Plant.Stats):

        def __init__(self) -> None:
            super().__init__()
            self._shade_count = 0

        def increment_shade(self) -> None:
            self._shade_count += 1

        def show_stats(self, name: str) -> None:
            super().show_stats(name)
            print(f"{self._shade_count} shade")

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of ", end='')
        print(f"{self._height:.1f}cm long and ", end='')
        print(f"{self.trunk_diameter:.1f}cm wide.")
        self._stats.increment_shade()

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):

    def __init__(
            self,
            name: str,
            height: float,
            days: int,
            growth_rate: float,
            harvest_season: str,
            ) -> None:
        super().__init__(name, height, days, growth_rate)
        self.nutritional_value = 0
        self.harvest_season = harvest_season

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


def display_stats(plant: Plant) -> None:
    plant._stats.show_stats(plant.name)


if __name__ == "__main__":
    print("=== Garden statistics ===")
    test_age1 = 30
    test_age2 = 400
    print("=== Check year-old")
    print(f"Is {test_age1} days more than a year? ->", end='')
    print(f" {Plant.year_old(test_age1)}")
    print(f"Is {test_age2} days more than a year? ->", end='')
    print(f" {Plant.year_old(test_age2)}\n")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red", 8.0)
    rose.show()
    display_stats(rose)
    rose.grow()
    rose.bloom()
    rose.show()
    display_stats(rose)

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_stats(oak)
    oak.produce_shade()
    display_stats(oak)

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow", 30.0)
    sunflower.show()
    sunflower.grow()
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_stats(sunflower)

    print("=== Anonymous")
    unknown = Plant.create_anonymous()
    unknown.show()
    display_stats(unknown)
