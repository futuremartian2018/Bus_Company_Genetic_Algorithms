# FUNCTION THAT ESTIMATES INDIVIDUAL FITNESS
def fitness(unit):
    for i in range(len(unit)):
        unit[i].fitness = unit[i].gain / 100 + 5 * unit[i].happy
    return unit