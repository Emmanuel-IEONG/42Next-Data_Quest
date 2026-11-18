import random


ACHIEVEMENTS = [
    "Crafting Genius",
    "World Savior",
    "Master Explorer",
    "Collector Supreme",
    "Untouchable",
    "Boss Slayer",
    "Strategist",
    "Speed Runner",
    "Survivor",
    "Treasure Hunter",
    "Unstoppable",
    "Sharp Mind",
    "First steps",
]


def gen_player_achievements() -> set[str]:
    random_number = random.randint(4, len(ACHIEVEMENTS))
    achievements = set(random.sample(ACHIEVEMENTS, random_number))
    achievements = achievements.union({'Common Power Up'})
    return (achievements)


def display_players_achievements(players: list[tuple[str, set[str]]]) -> None:
    for player_name, player_achievements in players:
        print(f"Player {player_name}: {player_achievements}")


def track_all_achievement(players: list[tuple[str, set[str]]]) -> None:
    all_achievement: set[str] = set()
    for _, player_achievements in players:
        all_achievement = all_achievement.union(player_achievements)
    print(f"\nAll distinct achievements: {all_achievement}")


def track_common_achievement(players: list[tuple[str, set[str]]]) -> None:
    commons: set[str] = players[0][1]
    for _, player_achievements in players[1:]:
        commons = commons.intersection(player_achievements)
    print(f"\nCommon achievements: {commons}\n")


def track_unique_achievement(players: list[tuple[str, set[str]]]) -> None:
    for i in range(len(players)):
        player_name, player_achievements = players[i]
        other_players = players[:i] + players[i + 1:]
        other_achievements: set[str] = set()
        for _, achievements in other_players:
            other_achievements = other_achievements.union(achievements)
        unique_achievement = player_achievements.difference(other_achievements)
        print(f"Only {player_name} has: {unique_achievement}")


def track_missing_achievements(players: list[tuple[str, set[str]]]) -> None:
    print()
    for player_name, achievements in players:
        missing_achievements = set(ACHIEVEMENTS).difference(achievements)
        print(f"{player_name} is missing: {missing_achievements}")


def main() -> None:
    print("=== Achievement Tracker System ===")
    players_list: list[tuple[str, set[str]]] = [
        ("Alice", gen_player_achievements()),
        ("Bob", gen_player_achievements()),
        ("Charlie", gen_player_achievements()),
        ("Dylan", gen_player_achievements()),
    ]
    display_players_achievements(players_list)
    track_all_achievement(players_list)
    track_common_achievement(players_list)
    track_unique_achievement(players_list)
    track_missing_achievements(players_list)


if __name__ == "__main__":
    main()
