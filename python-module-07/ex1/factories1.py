from ex0.factories0 import CreatureFactory
from . import creatures1


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> creatures1.Sproutling:
        return creatures1.Sproutling()

    def create_evolved(self) -> creatures1.Bloomelle:
        return creatures1.Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> creatures1.Shiftling:
        return creatures1.Shiftling()

    def create_evolved(self) -> creatures1.Morphagon:
        return creatures1.Morphagon()
