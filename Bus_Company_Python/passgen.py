# FUNCTION GENERATING PASSENGERS WITH THEIR STARTING AND TARGET CITIES

# Importing necessery class definitions and functions
import town
import random as ran
import distance as dist

def passgen(cit_num, max_seats, towns):
    pass_num = max_seats * 2 # Number of passengers in a single city
    cit_ind = list(range(cit_num))
    passg = []
    for i in range(cit_num):
        for j in range(pass_num):
            passg.append(town.Passg())
            passg[pass_num * i + j].start = i
            passg[pass_num * i + j].target = cit_ind[ran.randint(0, cit_ind[-1])] 

            while passg[pass_num * i + j].target == i: # start and target cities have to be different
                passg[pass_num * i + j].target = cit_ind[ran.randint(0, cit_ind[-1])]

            # passenger payment
            passg[pass_num * i + j].gain = gain(towns[passg[pass_num * i + j].start], towns[passg[pass_num * i + j].target])

    return passg


# FUNCTION THAT CALCULATES PASSENGER PAYMENT

def gain(start, target):
    gain_coef = 3.20 # cost per unit of distance
    return gain_coef * dist.distance(start, target)