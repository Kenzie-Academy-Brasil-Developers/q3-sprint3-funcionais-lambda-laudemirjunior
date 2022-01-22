from pytest import fixture
from faker import Faker
from random import randint


@fixture(scope="module")
def char_name() -> str:
    faker: Faker = Faker()

    return (faker.name() for _ in range(21))


@fixture(scope="module")
def generate_twenty_chars(char_name) -> list[dict]:
    all_chars: list[dict] = list()
    intelligence_chars: list[dict] = list()
    power_chars: list[dict] = list()
    strength_chars: list[dict] = list()
    agility_chars: list[dict] = list()

    value: int = randint(11, 200)

    for index, name in enumerate(char_name):
        new_char: dict = {
            "id": index,
            "name": name,
            "intelligence": value if index in [1, 5, 9, 13, 17] else 10,
            "power": value if index in [2, 6, 10, 14, 18] else 10,
            "strength": value if index in [3, 7, 11, 15, 19] else 10,
            "agility": value if index in [4, 8, 12, 16, 20] else 10,
        }

        if index:
            all_chars.append(new_char)

        if index in [1, 5, 9, 13, 17] and index:
            intelligence_chars.append(new_char)

        if index in [2, 6, 10, 14, 18] and index:
            power_chars.append(new_char)

        if index in [3, 7, 11, 15, 19] and index:
            strength_chars.append(new_char)

        if index in [4, 8, 12, 16, 20] and index:
            agility_chars.append(new_char)

    sum_of_all_powers: int = sum([char["power"] for char in all_chars])

    return (
        (
            all_chars,
            sum_of_all_powers,
        ),
        (
            intelligence_chars,
            value,
        ),
        (
            power_chars,
            value,
        ),
        (
            strength_chars,
            value,
        ),
        (
            agility_chars,
            value,
        ),
    )
