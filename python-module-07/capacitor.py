from ex1 import HealingCreatureFactory, TransformCreatureFactory


def main() -> None:
    healing_factory = HealingCreatureFactory()
    sproutling = healing_factory.create_base()
    bloomelle = healing_factory.create_evolved()

    transform_factory = TransformCreatureFactory()
    shiftling = transform_factory.create_base()
    morphagon = transform_factory.create_evolved()

    print("Testing Creature with healing capability")
    print("base:")
    print(sproutling.describe())
    print(sproutling.attack())
    print(sproutling.heal())

    print("\nevolved:")
    print(bloomelle.describe())
    print(bloomelle.attack())
    print(bloomelle.heal())

    print("\nTesting Creature with transform capability")
    print("base:")
    print(shiftling.describe())
    print(shiftling.attack())
    print(shiftling.transform())
    print(shiftling.attack())
    print(shiftling.revert())

    print("\nevolved:")
    print(morphagon.describe())
    print(morphagon.attack())
    print(morphagon.transform())
    print(morphagon.attack())
    print(morphagon.revert())


if __name__ == "__main__":
    main()
