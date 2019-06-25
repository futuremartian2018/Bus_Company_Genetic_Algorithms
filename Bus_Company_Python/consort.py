# FUNCTION THAT HELPS TO SORT CITIES AND THEIR CONNECTIONS

# Importing necessary class definitions and functions
import town
import distance as dist

def consort(ind_x, ind_y, weight, cit_num, map):
    citcon = []
    for j in range(cit_num):
        tab = []
        for i in range(len(ind_x)):
            if (ind_x[i] == j):
                temp = (ind_y[i], weight[i] * dist.distance(map[ind_x[i]], map[ind_y[i]]))
                tab.append(temp)
            elif (ind_y[i] == j):
                temp = (ind_x[i], weight[i] * dist.distance(map[ind_x[i]], map[ind_y[i]]))
                tab.append(temp)

        citcon.append(town.Conect())
        citcon[-1].neib = tab # assignment of cities neighbours

    return citcon