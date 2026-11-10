import sys


def main():
    arg_list = sys.argv
    len_list = len(arg_list)
    print("=== Command Quest ===")
    print(f"Program name: {arg_list[0]}")
    if (len_list <= 1):
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len_list - 1}")
        i = 1
        while (i < len_list):
            print(f"Argument {i}: {arg_list[i]}")
            i += 1
    print(f"Total arguments: {len_list}")


if __name__ == "__main__":
    main()
