# FUNCTION THAT SELECTS THE BEST BUS COMPANY IN CURRENT GENERATION

# Importing required functions and class definitions
import operator as op


def best(parent):
    p_fit = []
    for i in range(len(parent)):
        p_fit.append((parent[i].fitness, i))
    p_sort = sorted(p_fit, key = op.itemgetter(0), reverse = True)
    return parent[p_sort[0][1]]

# FUNCTION THAT SELECTS THE BEST BUS IN CURRENT GENERATION


def best_bus(parent):
    best_buses = []
    for i in range(len(parent)):
        buses = []
        for j in range(len(parent[i].fleet)):
            buses.append((j, parent[i].fleet[j].fitness))
        temp = sorted(buses, key = op.itemgetter(1))
        best_buses.append((i, temp[-1][0], temp[-1][1]))
    best_sorted = sorted(best_buses, key = op.itemgetter(2))
    return parent[best_sorted[-1][0]].fleet[best_sorted[-1][1]]

# FUNCTION THAT SELECTS THE BEST BUS OVERALL


def dominant(alpha, contender):

    if alpha.fitness < contender.fitness:
        alpha = contender
    return alpha


def dominants(val, contender):

    if val < contender.fitness:
        val = contender.fitness
        change = True
    else:
        change = False
    return val, change
