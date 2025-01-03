import pytest  # type: ignore
from letter_combinations_phone_number import letterCombinations as letter_combinations
from typing import List


@pytest.mark.parametrize(
    "digits, expected",
    [
        ("", []),
        ("2", ["a", "b", "c"]),
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
        (
            "79",
            [
                "pw",
                "px",
                "py",
                "pz",
                "qw",
                "qx",
                "qy",
                "qz",
                "rw",
                "rx",
                "ry",
                "rz",
                "sw",
                "sx",
                "sy",
                "sz",
            ],
        ),
        (
            "234",
            [
                "adg",
                "adh",
                "adi",
                "aeg",
                "aeh",
                "aei",
                "afg",
                "afh",
                "afi",
                "bdg",
                "bdh",
                "bdi",
                "beg",
                "beh",
                "bei",
                "bfg",
                "bfh",
                "bfi",
                "cdg",
                "cdh",
                "cdi",
                "ceg",
                "ceh",
                "cei",
                "cfg",
                "cfh",
                "cfi",
            ],
        ),
        (
            "2345",
            [
                "adgj",
                "adgk",
                "adgl",
                "adhj",
                "adhk",
                "adhl",
                "adij",
                "adik",
                "adil",
                "aegj",
                "aegk",
                "aegl",
                "aehj",
                "aehk",
                "aehl",
                "aeij",
                "aeik",
                "aeil",
                "afgj",
                "afgk",
                "afgl",
                "afhj",
                "afhk",
                "afhl",
                "afij",
                "afik",
                "afil",
                "bdgj",
                "bdgk",
                "bdgl",
                "bdhj",
                "bdhk",
                "bdhl",
                "bdij",
                "bdik",
                "bdil",
                "begj",
                "begk",
                "begl",
                "behj",
                "behk",
                "behl",
                "beij",
                "beik",
                "beil",
                "bfgj",
                "bfgk",
                "bfgl",
                "bfhj",
                "bfhk",
                "bfhl",
                "bfij",
                "bfik",
                "bfil",
                "cdgj",
                "cdgk",
                "cdgl",
                "cdhj",
                "cdhk",
                "cdhl",
                "cdij",
                "cdik",
                "cdil",
                "cegj",
                "cegk",
                "cegl",
                "cehj",
                "cehk",
                "cehl",
                "ceij",
                "ceik",
                "ceil",
                "cfgj",
                "cfgk",
                "cfgl",
                "cfhj",
                "cfhk",
                "cfhl",
                "cfij",
                "cfik",
                "cfil",
            ],
        ),
    ],
)
def test_letter_combinations(digits: str, expected: List[str]):
    result = letter_combinations(digits)
    assert (
        result == expected
    ), f"digits: {digits}, expected: {expected}, result: {result}"
