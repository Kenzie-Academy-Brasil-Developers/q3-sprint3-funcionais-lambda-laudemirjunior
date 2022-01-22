from main import team_power_2
from random import randint


def test_sum_of_all_team_power(generate_twenty_chars: list[dict]) -> None:
    all_chars, _, _, _, _ = generate_twenty_chars
    chars, value = all_chars

    adv: int = randint(1, 10000)
    expected: int = value + adv

    result: int = team_power_2(chars, adv)

    assert result == expected
