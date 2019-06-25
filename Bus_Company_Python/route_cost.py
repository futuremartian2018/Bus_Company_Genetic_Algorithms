# FUNCTION THAT ESTIMATES COST OF EVERY BUSES ROUTE

def routecost(parent, citcon):
    for i in range(len(parent)):
        total = 0
        for j in range(len(parent[i].fleet)):
            temp_sum = 0
            for k in range(len(parent[i].fleet[j].track) - 1 ):
                track = parent[i].fleet[j].track  # route of a particular bus
                neib = citcon[track[k]].neib      # current cities neighbours
                for n in range(len(neib)):
                    if neib[n][0] == track[k + 1]: # if a particular neighbour is part of a track 
                        temp_sum += neib[n][1]     # then add connection cost
                        break
            parent[i].fleet[j].cost = temp_sum # cost for a single bus
            total += temp_sum
        parent[i].cost = total # cost for a whole bus company
    return parent