# FUNCTION THAT CALCULATES DISTANCE BETWEEN TWO GIVEN CITIES

def distance(cit1, cit2):
    dx = cit1.x - cit2.x
    dy = cit1.y - cit2.y
    return (dx ** 2 + dy ** 2) ** 0.5