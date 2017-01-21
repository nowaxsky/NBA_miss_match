# miss_match definition

# When PG throws a ball, the closest defender is a miss-match player.
def attack_mm_PG(defend):
    if defend >= 5:
        return 1
    else:
        return 0

# When C throws a ball, the closest defender is a miss-match player.		
def attack_mm_C(defend):
    if defend <= 2:
        return 1
    else:
        return 0

# When SG throws a ball, the closest defender is a miss-match player.		
def attack_mm_SG(defend):
    if defend >= 5:
        return 1
    else:
        return 0

# When PF throws a ball, the closest defender is a miss-match player.
def attack_mm_PF(defend):
    if defend <= 2:
        return 1
    else:
        return 0