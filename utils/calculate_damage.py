from type_multiplier import type_multiplier
import random

def calculate_damage(attacker, defender, type_chart):
    # Your code goes here
    # the attacker uses its best attack stat against the matching defense stat
    if attacker["attack"] >= attacker["sp_atk"]:
        atk = attacker["attack"]
        dfn = defender["defense"]
    else:
        atk = attacker["sp_atk"]
        dfn = defender["sp_def"]

    base_damage = ((42 * 60 * atk / dfn) / 50) + 2

    # type effectiveness and random factor
    multiplier = type_multiplier(attacker["types"], defender["types"], type_chart)
    damage = base_damage * multiplier * random.uniform(0.85, 1.0)

    # damage must be an integer and at least 1
    damage = max(1, int(damage))
    return damage, multiplier
