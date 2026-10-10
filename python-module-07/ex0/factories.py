from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from . import creatures

T = TypeVar("T")

class CreatureFactory(ABC, Generic[T]):
    @abstractmethod
    def created_base(self) -> str:
        ...

    @abstractmethod
    def created_evolve(self) -> str:
        ...


class FlameFactory(CreatureFactory):
    def created_base(self) -> str:

    def created_evolve(self) -> str:


class AquaFactory(CreatureFactory):
    def created_base(self) -> str:

    def created_evolve(self) -> str:
