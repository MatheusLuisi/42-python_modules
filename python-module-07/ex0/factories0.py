from abc import ABC, abstractmethod
from . import creatures0


class CreatureFactory(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def create_base(self) -> creatures0.Creature:
        ...

    @abstractmethod
    def create_evolved(self) -> creatures0.Creature:
        ...


class FlameFactory(CreatureFactory):
    def create_base(self) -> creatures0.Creature:
        return creatures0.Flameling()

    def create_evolved(self) -> creatures0.Creature:
        return creatures0.Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> creatures0.Creature:
        return creatures0.Aquabub()

    def create_evolved(self) -> creatures0.Creature:
        return creatures0.Torragon()
