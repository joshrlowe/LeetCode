import pytest  # type: ignore
from Python.climbing_stairs_solution_1 import climbStairs as climb_stairs_1
from Python.climbing_stairs_solution_2 import climbStairs as climb_stairs_2


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
        (6, 13),
        (7, 21),
        (8, 34),
        (9, 55),
        (10, 89),
        (20, 10946),
        (30, 1346269),
        (35, 14930352),
        (40, 165580141),
        (45, 1836311903),
    ],
)
def test_climb_stairs(n: int, expected: int) -> None:
    result_1 = climb_stairs_1(n)
    assert result_1 == expected, f"n: {n}, expected: {expected}, result: {result_1}"

    result_2 = climb_stairs_2(n)
    assert result_2 == expected, f"n: {n}, expected: {expected}, result: {result_2}"
