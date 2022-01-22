from main import team_power


def test_sum_of_all_team_power(generate_twenty_chars: list[dict]) -> None:
    all_chars, _, _, _, _ = generate_twenty_chars
    chars, expected = all_chars

    result: int = team_power(chars)

    assert result == expected
