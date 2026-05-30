# Practice: type hints on simple functions


def add_numbers(a: int, b: int) -> int:
    return a + b


def get_username(user_id: int) -> str:
    return f"user_{user_id}"


def process_scores(scores: list[float]) -> dict[str, float]:
    return {"mean": sum(scores) / len(scores), "max": max(scores)}


def find_user(user_id: int) -> str | None:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)
