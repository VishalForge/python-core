import pytest

# The functions we're testing
def add(a: int, b:int) -> int:
    return a + b

def divide(a: float, b:float) -> float | None:
    if b == 0:
        return None
    return a / b

def get_grade(score: int) -> str:
    if score >= 90:
        return "A"
    elif score >= 70:
        return "B"
    else:
        return "C"


# The tests
def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -1) == -2

def test_divide_normal():
    assert divide(10, 2) == 5.0

def test_divide_by_zero_returns_none():
    assert divide(5, 0) is None

@pytest.mark.parametrize("score,expected", [
    (95, "A"),
    (75, "B"),
    (60, "C"),
    (90, "A"),
    (70, "B")
])
def test_get_grade(score, expected):
    assert get_grade(score) == expected