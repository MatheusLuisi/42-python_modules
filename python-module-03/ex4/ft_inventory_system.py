#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_inventory_system.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/10 14:15:56 by mpinto-l            #+#    #+#            #
#   Updated: 2026/08/10 14:16:09 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


def main() -> None:
    arguments = sys.argv[1:]
    inventory: dict[str, int] = {}

    print("=== Inventory System Analysis ===")

    for argument in arguments:
        parts = argument.split(':')
        if len(parts) != 2:
            print(f"Error - invalid parameter '{argument}'")
            continue

        item_name, quantity_str = parts[0], parts[1]

        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarding")
            continue

        try:
            quantity = int(quantity_str)
            inventory[item_name] = quantity
        except ValueError as error:
            print(f"Quantity error for '{item_name}': {error}")

    print(f"\nGot inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")

    total_quantity = sum(inventory.values())

    print(f"\nTotal quantity of the {len(inventory)} items: {total_quantity}")

    for item_name in inventory.keys():
        item_quantity = inventory[item_name]
        if total_quantity > 0:
            percentage = (item_quantity / total_quantity) * 100
            print(f"Item {item_name} represents {round(percentage, 1)}%")
    if inventory:
        item_names = list(inventory.keys())
        most_abundant_item = item_names[0]
        least_abundant_item = item_names[0]

        for item_name in item_names:
            if inventory[item_name] > inventory[most_abundant_item]:
                most_abundant_item = item_name
            if inventory[item_name] < inventory[least_abundant_item]:
                least_abundant_item = item_name

        print(
            f"\nItem most abundant: {most_abundant_item} "
            f"with quantity {inventory[most_abundant_item]}"
        )
        print(
            f"Item least abundant: {least_abundant_item} "
            f"with quantity {inventory[least_abundant_item]}"
        )

    inventory.update({"magic_item": 1})

    print(f"\nUpdated inventory: {inventory}")


if __name__ == "__main__":
    main()
