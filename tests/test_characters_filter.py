from main import characters_filter


def test_charactres_filtering_by_intelligence(
    generate_twenty_chars: list[dict],
) -> None:
    all_chars, intelligence, _, _, _ = generate_twenty_chars
    chars, _ = all_chars
    expected, value = intelligence

    response: list = characters_filter(chars, "intelligence", value)

    assert response == expected


def test_charactres_filtering_by_power(
    generate_twenty_chars: list[dict],
) -> None:
    all_chars, _, power, _, _ = generate_twenty_chars
    chars, _ = all_chars
    expected, value = power

    response: list = characters_filter(chars, "power", value)

    assert response == expected


def test_charactres_filtering_by_strength(
    generate_twenty_chars: list[dict],
) -> None:
    all_chars, _, _, strength, _ = generate_twenty_chars
    chars, _ = all_chars
    expected, value = strength

    response: list = characters_filter(chars, "strength", value)

    assert response == expected


def test_charactres_filtering_by_agility(
    generate_twenty_chars: list[dict],
) -> None:
    all_chars, _, _, _, agility = generate_twenty_chars
    chars, _ = all_chars
    expected, value = agility

    response: list = characters_filter(chars, "agility", value)

    assert response == expected
