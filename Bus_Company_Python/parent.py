# FUNCTION GENERATING A BUS WITH ITS SEAT NUMBER AND TRACKS

# Importing required functions and class definitions
import town
import random as ran

def parent(bus_num, cit_num, citcon, max_seats):
    # Assignment of randomly selected starting city, number of seats and route length
    bus_route = [town.Bus(ran.randint(0, cit_num), ran.randint(5, max_seats), ran.randint(3, int(cit_num / 5))) for i in range(bus_num)]

    # ROUTE SELECTION
    max_route = list(range(cit_num))
    for i in range(bus_num):
        track = []
        k = 0
        if(bus_route[i].start + bus_route[i].length <= cit_num):
            bus_route[i].track = max_route[bus_route[i].start : bus_route[i].start + bus_route[i].length ]
        else:
            track = max_route[bus_route[i].start : -1]
            if track == []:
                track = [max_route[-1]]
       
            cities_left = bus_route[i].length - len(track)
            index = track[-1]
                
            while k < cities_left:
                last = citcon[index].neib
                choose = [last[i][0] for i in range(len(last))]
                choose = cremove(choose, track)
                chsort = sorted(choose)
                if chsort == []:
                    break
                track.append(chsort[0])
                k += 1
            bus_route[i].track = track
        bus_route[i].length = len(bus_route[i].track)
    return bus_route



# REMOVE CITIES THAT BUS HAS ALREADY TRAVELLED TO
def cremove(choose, track):
    remain = []
    for i in range(len(choose)):
        for j in range(len(track)):
            if choose[i] == track[j]:
                choose[i] = -12 

    for k in range(len(choose)):
        if choose[k] != -12:
            remain.append(choose[k])
    return remain