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


def main() -> None:
    print("=== Inventory System Analysis ===")
    argv = sys.argv
    inventory = parse_command_line(argv)
    print(f"Inventory: {inventory}")


if __name__ == "__main__":
    main()
