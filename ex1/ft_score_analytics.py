import sys


class NoArgumentError(Exception):
    def __init__(self):
        super().__init__("No scores provided. Usage: python3 "
                         "ft_score_analytics.py <score1> <score2> ...")


def main():
    print("=== Player Score Analytics ===")
    argv = sys.argv
    argv.pop(0)
    score_list = []
    for element in argv:
        try:
            score_list.append(int(element))
        except ValueError:
            print(f"Invalid parameter: '{element}'")

    len_list = len(score_list)

    def display_score():
        if not score_list:
            raise NoArgumentError
        total_score = sum(score_list)
        average_score = total_score / len_list
        max_score = max(score_list)
        min_score = min(score_list)
        range_score = max_score - min_score

        print(f"Scores processed: {score_list}")
        print(f"Total players: {len_list}")
        print(f"Total score: {total_score}")
        print(f"Average score: {average_score}")
        print(f"High score: {max_score}")
        print(f"Low score: {min_score}")
        print(f"Score range: {range_score}")

    try:
        display_score()
    except NoArgumentError as err:
        print(err)


if __name__ == "__main__":
    main()
