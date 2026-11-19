import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players: list[str] = ["alice", "bob", "charlie", "dylan"]
    actions: list[str] = ["run", "eat", "sleep", "grab", "move", "climb",
                          "swim", "use", "release"]
    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield ((name, action))


def consume_event(
        events: list[tuple[str, str]]
        ) -> Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        event = random.choice(events)
        events.remove(event)
        yield (event)


def main() -> None:
    event_stream = gen_event()

    for i in range(1000):
        name, action = next(event_stream)
        print(f"Event {i}: Player {name} did action {action}")

    events: list[tuple[str, str]] = []
    for _ in range(10):
        events.append(next(event_stream))
    print(f"Built list of 10 events: {events}")

    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()
