# FUNCTION RESPONSIBLE FOR PARENT CROSSOVER

# Importing necessery class definitions and functions
import random as ran
import town

def cross(parent):
    p_num = len(parent)
    b_num = len(parent[0].fleet)
    parent_ind = []
    bus_ind = []
    crossed = []
    k = 0
    # saving indexes
    for i in range(p_num):
        for j in range(b_num):
            parent_ind.append(i)
            bus_ind.append(j)
    # shuffleing indexes
    while k < 5:
        ran.shuffle(parent_ind)
        ran.shuffle(bus_ind)
        k += 1
    # crossover
    for i in range(p_num):
        crossed.append(town.Parent())
        for j in range(b_num):
            crossed[i].fleet.append(parent[parent_ind[i]].fleet[bus_ind[j]])

    return crossed