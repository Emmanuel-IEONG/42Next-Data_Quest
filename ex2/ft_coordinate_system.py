import math


def get_player_pos() -> tuple:
    while True:
        try:
            coordinates = input('Enter new coordinates as floats in '
                                'format \'x,y,z\':').strip()
            coord_split = coordinates.split(',')
            if (len(coord_split) != 3):
                raise SyntaxError

            coord_tuple: tuple[float, ...] = ()
            for element in coord_split:
                coord_tuple += (float(element),)

            return (coord_tuple)
        except SyntaxError:
            print("Invalid syntax")
        except ValueError as err:
            print(f"Error on parameter '{element}': {err}")


def calculate_distance(first: tuple, second: tuple) -> float:
    return (math.sqrt((second[0] - first[0])**2 +
            (second[1] - first[1])**2 + (second[2] - first[2])**2))


def main():
    print("=== Game Coordinate System ===")
    print("\nGet a first set of coordinates")
    t1 = get_player_pos()
    print(f"Got a first tuple: {t1}")
    print(f"It includes: X={t1[0]}, Y={t1[1]}, Z={t1[2]}")
    print(f"Distance to center: {round(calculate_distance(t1, (0, 0, 0)), 4)}")

    print("\nGet a second set of coordinates")
    t2 = get_player_pos()
    print(f"Distance between the 2 sets of coordinates: "
          f"{round(calculate_distance(t1, t2), 4)}")


if __name__ == "__main__":
    main()
