import sys


class KeyError(Exception):
    def __init__(self, message):
        super().__init__(f"{message}")


def parse_command_line(argv: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = dict()
    for element in argv[1:]:
        try:
            key, value = element.split(":")
        except ValueError:
            print(f"Error - invalid parameter '{element}'")
            continue

        try:
            if key in inventory:
                raise KeyError(f"Redundant item '{key}' - discarding")
            inventory[key] = int(value)
        except KeyError as err:
            print(err)
        except ValueError as err:
            print(f"Quantity error for '{key}': {err}")
    return (inventory)


def count_items(inventory: dict[str, int]) -> int:
    display_list: list[str] = []
    total_quantity: int = 0
    for item, quantity in inventory.items():
        display_list.append(item)
        total_quantity += quantity
    print(f"\nItem list: {display_list}")
    print(f"Total quantity of the {len(display_list)} items: {total_quantity}")
    return (total_quantity)


def calculate_percentage(inv: dict[str, int], total_quantity: int) -> None:
    first_key, first_value = list(inv.items())[0]
    max_key = min_key = first_key
    max_value = min_value = first_value
    for item, quantity in inv.items():
        percentage: float = quantity * 100 / total_quantity
        print(f"Item {item} represents {round(percentage, 1)}%")
        if quantity > max_value:
            max_key, max_value = item, quantity
        elif quantity < min_value:
            min_key, min_value = item, quantity
    print(f"\nItem most abundant: {max_key} with quantity {max_value}")
    print(f"Item least abundant: {min_key} with quantity {min_value}")


def add_item(inv: dict[str, int], item_name: str, quantity: int) -> None:
    inv[item_name] = quantity


def main() -> None:
    print("=== Inventory System Analysis ===")
    argv = sys.argv
    inventory = parse_command_line(argv)
    print(f"Got inventory: {inventory}")
    total_quantity = count_items(inventory)
    calculate_percentage(inventory, total_quantity)
    add_item(inventory, "magic_item", 1)
    print(f"\nUpdated inventory: {inventory}")


if __name__ == "__main__":
    main()
