# FUNCTION THAT SELECTS PASSENGERS AND ESTIMATES GAIN

# Importing required functions and class definitions
import operator as op
import town

def passselect(passengers, parent):
    start = [passengers[s].start for s in range(len(passengers))]
    target = [passengers[t].target for t in range(len(passengers))]
    gain = [passengers[g].gain for g in range(len(passengers))]
    
    for i in range(len(parent)):
        total = 0
        p_total = 0
        for j in range(len(parent[i].fleet)):
            temp_sum = 0
            p_sum = 0
            city = parent[i].fleet[j].start
            seats = parent[i].fleet[j].seats

            # sorting passengers according to how much a company will earn
            m_start = selectbycity(start, city, start)
            m_end = selectbycity(start, city, target)
            p_gain = selectbycity(start, city, gain)
            group = groups(m_start, m_end, p_gain)
            sorted_group = sorted(group, key = op.itemgetter(2), reverse = True)
            selpass = []
            if group == []:
                break
            for k in range(seats):
                selpass.append(town.Passg())
                selpass[k].start = sorted_group[k][0]
                selpass[k].target = sorted_group[k][1]
                selpass[k].gain = sorted_group[k][2]
                # checking if passengers target city is on bus track
                if( check(selpass[k].target, parent[i].fleet[j].track) == True):
                    temp_sum += selpass[k].gain
                    p_sum += 1
                

            # calculating gain of a bus
            parent[i].fleet[j].take = temp_sum
            parent[i].fleet[j].gain = parent[i].fleet[j].take - parent[i].fleet[j].cost
            parent[i].fleet[j].happy = p_sum
            p_total += p_sum
            total += temp_sum

        # calculating company's gain
        parent[i].take = total
        parent[i].gain = parent[i].take - parent[i].cost
        parent[i].happy = p_total
        parent[i].ind = i

    return parent

        
# FUNCTION THAT SELECTS FIELDS BASED ON STARTING CITY 
def selectbycity(start, bus_start, reduce):
    reduced = []
    for i in range(len(start)):
        if start[i] == bus_start:
            reduced.append(reduce[i])
    return reduced

# FUNCTION THAT CHECKS IF TARGET CITY IS ON BUSES TRACK
def check(aim, track):
    for i in range(len(track)):
        if track[i] == aim:
            logical = True
            break
        else:
            logical = False
    return logical

# FUNCTION GROUPING PASSENGER INFORMATION
def groups(start, target, gain):
    group = []
    for i in range(len(start)):
        group.append((start[i], target[i], gain[i]))
    return group