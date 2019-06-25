# BUS COMPANIES - GENETIC ALGORITHMS - ARKADIUSZ MARTA  © 2019

# Importing required functions and class definitions
import town
import mapgen
import roads
import random
import distance
import passgen as pas
import consort as con
import parent as par
import route_cost as rc
import pass_select as pc
import fitness as fit
import best
import mutate as mut
import cross as cs
import numpy as np
import matplotlib.pyplot as plt

# GENERATING A GRAPH REPRESENTING ENTIRE MAP
cit_num = 31 # number of cities on a map
graph = []
graph = mapgen.mapgen(cit_num, graph) # generating cities and their coordinates
x, y, w = roads.roads(graph) # generating connections between cities
# GENERATING PASSENGERS

pos_x = [graph[i].x for i in range(len(graph))]
pos_y = [graph[i].y for i in range(len(graph))]

plt.figure(1, figsize=(10, 6))
plt.plot(pos_x, pos_y, 'ro')
plt.title('CITIES GRAPH')
for i in range(len(pos_x)):
    plt.text(pos_x[i], pos_y[i], str(graph[i].indeks), fontsize=14)

for i in range(len(x)):
    p1 = [graph[x[i]].x, graph[y[i]].x]
    p2 = [graph[x[i]].y, graph[y[i]].y]
    plt.plot(p1, p2, 'g')
plt.axis('off')
plt.pause(0.05)


max_load = 25 # maximum  number of passengers
passengers = pas.passgen(cit_num, max_load, graph)

# GENERATING BUSES AND THEIR ROUTES
unit_num = 10 # number of selection units
bus_num = 5 # number of buses
unit_parent = []
citcon = con.consort(x, y, w, cit_num, graph) # cities and their neighbours grouped
# Generating Parents - Bus companies
for i in range(unit_num):
    unit_parent.append(town.Parent())
    unit_parent[i].fleet = par.parent(bus_num, cit_num, citcon, max_load)

# Base fitness values before genetic algorithm implementation
best_drive = []
best_unit = town.Parent()
best_unit.fitness = - 100000
best_unit_fitness = []
best_drive_fitness = []

best_fit = -10000

# GENETIC ALGORITHM
for gn in range(150):

    # CALCULATING ROUTE COST
    unit_parent = rc.routecost(unit_parent, citcon)

    # SELECTION OF PASSENGERS AND GAIN ESTIMATION
    unit_parent = pc.passselect(passengers, unit_parent)

    # FITNESS ESTIMATION
    #parent fitness
    unit_parent = fit.fitness(unit_parent) 
    # bus fitness
    for i in range(len(unit_parent)):
        unit_parent[i].fleet = fit.fitness(unit_parent[i].fleet)

    # BEST UNIT SELECTION
    # the best bus in current generation
    contender_bus = best.best_bus(unit_parent)
    best_fit, change = best.dominants(best_fit, contender_bus)
    best_drive_fitness.append(best_fit)

    # the best bus company in current generation
    contender = best.best(unit_parent)
    best_unit = best.dominant(best_unit, contender)
    best_unit_fitness.append(best_unit.fitness)

    # ROUTE MUTATION
    unit_child = mut.mutate(unit_parent, citcon)

    # PARENT'S CROSSOVER
    unit_crossed = cs.cross(unit_parent)

    # CROSSED INDIVIDUALS BECOME NEW PARENT GENERATION
    unit_parent = unit_crossed

    if change == True:
        plt.plot(pos_x, pos_y, 'ro')
        best_drive.append(contender_bus)
        ind_x, ind_y = town.track_map(best_drive[-1])
        for i in range(len(pos_x)):
            plt.text(pos_x[i], pos_y[i], str(graph[i].indeks), fontsize=14)
        for i in range(len(x)):
            p1 = [graph[x[i]].x, graph[y[i]].x]
            p2 = [graph[x[i]].y, graph[y[i]].y]
            plt.plot(p1, p2, 'g')
        for i in range(len(ind_x)):
            p1 = [graph[ind_x[i]].x, graph[ind_y[i]].x]
            p2 = [graph[ind_x[i]].y, graph[ind_y[i]].y]
            plt.plot(p1, p2, 'm')
        plt.axis('off')
        plt.pause(0.05)


# BEST INDIVIDUAL FITNESS CHART

plt.figure(2, figsize=(10, 6))
plt.subplot(121)
plt.title('BUS FITNESS CHART')
plt.plot(best_drive_fitness)
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.subplot(122)
plt.title('COMPANY FITNESS CHART')
plt.plot(best_unit_fitness)
plt.xlabel('Generation')
plt.ylabel('Fitness')


plt.show()