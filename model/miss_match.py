# miss_match definition
# {PG:1,SG:2,SF:3,PF:4,C:5}

## Offence miss match
# When PG throws a ball, the closest defender is a miss-match player.
def off_mm_PG(defence):
    if defence >= 4:
        return 1
    else:
        return 0

# When SG throws a ball, the closest defender is a miss-match player.		
def off_mm_SG(defence):
    if defence >= 5:
        return 1
    else:
        return 0

# When SF throws a ball, the closest defender is a miss-match player.
def off_mm_SF(defence):
    if (defence == 1) or (defence == 5):
        return 1
    else:
        return 0

# When PF throws a ball, the closest defender is a miss-match player.
def off_mm_PF(defence):
    if defence <= 1:
        return 1
    else:
        return 0

# When C throws a ball, the closest defender is a miss-match player.		
def off_mm_C(defence):
    if defence <= 2:
        return 1
    else:
        return 0
		

## Defence miss match
# When PG is in defend side, the closest player is a miss-match player.
def def_mm_PG(offence):
    if offence >= 4:
        return 1
    else:
        return 0

# When SG is in defend side, the closest player is a miss-match player.	
def def_mm_SG(offence):
    if offence >= 5:
        return 1
    else:
        return 0

# When SF is in defend side, the closest player is a miss-match player.
def def_mm_SF(offence):
    if (offence == 1) or (offence == 5):
        return 1
    else:
        return 0		
		
# When PF is in defend side, the closest player is a miss-match player.
def def_mm_PF(offence):
    if offence <= 1:
        return 1
    else:
        return 0

# When C is in defend side, the closest player is a miss-match player.	
def def_mm_C(offence):
    if offence <= 2:
        return 1
    else:
        return 0		