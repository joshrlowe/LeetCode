import pytest  # type: ignore
from Python.reverse_integer_solution_1 import reverse as solution_1
from Python.reverse_integer_solution_2 import reverse as solution_2


@pytest.mark.parametrize(
    "x, expected",
    [
        (123, 321),
        (-123, -321),
        (120, 21),
        (5, 5),
        (0, 0),
        (1534236469, 0),
        (-1534236469, 0),
    ],
)
def test_solutions(x, expected):
    result_1 = solution_1(x)
    assert result_1 == expected, f"x: {x}, expected: {expected}, result: {result_1}"

    result_2 = solution_2(x)
    assert result_2 == expected, f"x: {x}, expected: {expected}, result: {result_2}"
