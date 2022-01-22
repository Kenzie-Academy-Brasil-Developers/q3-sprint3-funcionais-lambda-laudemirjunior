from functools import reduce

def characters_filter(list_of_characters, key, value):
    return list(filter(lambda x: x[key] == value, list_of_characters))

def team_power(list_of_characters):
    return sum(map(lambda x: x['power'], list_of_characters))

def team_power_2(list_of_characters, advantage):
    return reduce(lambda acc, num: acc + num['power'], list_of_characters, advantage)