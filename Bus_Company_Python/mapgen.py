# FUNCTION THAT IS RESPONSIBLE FOR MAP GENERATIONS

# Importing 'random' library
import random
import town as tn

def mapgen(city_num, town):
    i = 0
    while (i < city_num):
        # GENERATING TOWNS AND THEIR LOCATIONS
        town.append(tn.Town())
        town[i].indeks = i
        town[i].x = random.uniform(-25, 25)
        town[i].y = random.uniform(-25, 25)
        # CHECKING IF THERE ARE TWO IDENTICAL CITIES
        for j in list(range(i + 1)):
            if(((town[i].x == town[j].x) and (town[i].y == town[j].y)) or j == i ):
                repeat = False
            else:
                repeat = True
        # IF THERE ARE NO SUCH CITIES THEN INCREMENT 'i' 
        if(repeat == False):
            i += 1
    return town