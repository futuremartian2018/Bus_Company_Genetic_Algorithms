# FUNCTION THAT GENERATES CONNECTIONS BETWEEN CITIES

# Importing 'random' library
import random
import operator as op
# Importing a function, that estimates distance beetween cities
import distance as dist

def roads(cities):
    loc_matrix = list(range(len(cities))) # list of indexes
    cit_num = len(loc_matrix)
    road_weight = [] # list of connection weights
    loc_x = [] # list of x-coordinates
    loc_y = [] # list of y-coordinates

    # CONNECTING EVERY CITY ON THE MAP
    for i in list(range(cit_num - 1)):
        loc_x.append(loc_matrix[i])
        loc_y.append(loc_matrix[i + 1])
        road_weight.append(random.randint(4, 8))

    # CONNECTING NEARBY CITIES TOGETHER
    # list describing probability of defined number of created connections in one iteration
    probability = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3] 

    for j in list(range(cit_num)):
        road = probability[ random.randint(0, len(probability) - 1) ]
        d=[]
        for k in list(range(cit_num)):
            temp = (dist.distance(cities[j], cities[k]), cities[j].indeks, cities[k].indeks)
            d.append(temp)
        d = sorted(d, key = op.itemgetter(0)) # sorting connections by distance
        for m in list(range(road)):
            loc_x.append(d[m + 1][1])
            loc_y.append(d[m + 1][2])
            road_weight.append(random.randint(4, 11))

    # DELETING REPEATING CONNECTIONS
    for p in list(range(len(loc_x))):
        for q in list(range(len(loc_y))):
            if((((loc_x[p] == loc_x[q]) and (loc_y[p] == loc_y[q])) or ((loc_x[p] == loc_y[q]) and (loc_y[p] == loc_x[q]))) and p != q):
                loc_x[p] = -12
                

    cor_x = [] # x-coordinates
    cor_y = [] # y -coordinates
    con_weight = []  # connection weights        

    for i in list(range(len(loc_x))):
        if loc_x[i] != -12:
            cor_x.append(loc_x[i])
            cor_y.append(loc_y[i])
            con_weight.append(road_weight[i])

    return cor_x, cor_y, con_weight