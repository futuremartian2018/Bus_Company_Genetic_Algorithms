# FUNCTION RESPONSIBLE FOR BUS MUTATIONS

# Importing necessery class definitions and functions
import town
import operator as op
import random as ran

def mutate(parent, citcon):
    child = []
    for i in range(len(parent)):
        child.append(town.Parent())
        mutation_subject = select(parent[i].fleet)
        for j in range(len([parent[i].fleet])):
            child[i].fleet.append(mutation_type(parent[i].fleet, mutation_subject, j, citcon))
    return child


# FUNCTION SELECTING BUSES FOR MUTATION - 2 BEST BUSES AND THE WORST ONE
def select(fleet):
    composition = []
    selected = []
    for i in range(len(fleet)):
        composition.append((i, fleet[i].fitness))
    composition = sorted(composition, key = op.itemgetter(1))
    selected.append(composition[-1][0])
    selected.append(composition[-2][0])
    selected.append(composition[0][0])
    return selected

# FUNCTION THAT RANDOMLY CHOOSES MUTATION TYPE
def mutation_type(fleet, subject, iter, citcon):
    size = len(fleet)
    if size % 2 == 0:
        weakest = 2
    else:
        weakest = 3
    iter_size = (size - weakest)/2
    m_type = ran.randint(0,2)

    # choose mutation subject according to iteration
    if iter <= iter_size:
        change = subject[0]
    elif iter > iter_size and iter <= 2*iter_size:
        change = subject[1]
    else:
        change = subject[2]

    # randomly choose mutation type
    if m_type == 0:
        mutant = len_mod(fleet[change], citcon)
    elif m_type == 1:
        mutant = inter_mod(fleet[change], citcon)
    else:
        mutant = boundary_mod(fleet[change], citcon)
    
    return mutant

# MUTATION OF ROUTE'S LENGTH
def len_mod(subject, citcon):
    len_change = ran.randint(0,2)
    if len_change == 0:
        track = subject.track
        if len(track) > 2:
            track.remove(track[-1])
            mutant = town.Bus(subject.start, subject.seats, len(track))
            mutant.track = track
        else:
            mutant = town.Bus(subject.start, subject.seats, subject.length)
            mutant.track = track
    elif len_change == 1:
        track = subject.track
        if len(track) < len(citcon):
            last = track[-1]
            possible = [citcon[last].neib[i][0] for i in range(len(citcon[last].neib))]
            swap = False
            for i in range(len(possible)):
                if check(possible[i], track) == False:
                    swap = False
                    track.append(possible[i])
                    break
                else:
                    swap = True
            if swap == True:
                first = track[0]
                possible = [citcon[first].neib[i][0] for i in range(len(citcon[first].neib))]
                for i in range(len(possible)):
                    if check(possible[i], track) == False:
                        track.insert(0, possible[i])
                        break
            mutant = town.Bus(track[0], subject.seats, len(track))
            mutant.track = track
        else:
            mutant = town.Bus(subject.start, subject.seats, subject.length)
            mutant.track = track
    else:
        mutant = town.Bus(subject.start, subject.seats, subject.length)
        mutant.track = subject.track
    return mutant

# MUTATION OF ROUTE'S INTERNAL CITIES
def inter_mod(subject, citcon):
    track = subject.track
    t_length = len(track)
    if t_length <= 3:
        mutant = town.Bus(subject.start, subject.seats, subject.length)
        mutant.track = track
    else:
        modified = ran.randint(1, (t_length - 1))
        shortened = [track[k] for k in range(modified)]
        required = t_length - len(shortened)
        m = 0
        kill = True
        while m < required:
            last = shortened[-1]
            possible = [citcon[last].neib[i][0] for i in range(len(citcon[last].neib))]
            for j in range(len(possible)):
                if check(possible[j], shortened) == False:
                    kill = False
                    shortened.append(possible[j])
                    break
                else:
                    kill = True
            if kill == True:
                break
            m += 1
        mutant = town.Bus(shortened[0], subject.seats, len(shortened))
        mutant.track = shortened
    return mutant

# MUTATION OF ROUTE'S BOUNDARY CITIES
def boundary_mod(subject, citcon):
    track = subject.track
    if len(track) < len(citcon):
        last = track[-2]
        possible = [citcon[last].neib[i][0] for i in range(len(citcon[last].neib))]
        swap = False
        for i in range(len(possible)):
            if(check(possible[i], track) == False):
                swap = False
                track[-1] = possible[i]
                break
            else:
                swap = True
        if swap == True:
            first = track[1]
            possible = [citcon[first].neib[i][0] for i in range(len(citcon[first].neib))]
            for j in range(len(possible)):
                if(check(possible[j], track) == False):
                    track[0] = possible[j]
                    break
        mutant = town.Bus(track[0], subject.seats, len(track))
        mutant.track = track
    else:
        mutant = town.Bus(subject.start, subject.seats, subject.length)
        mutant.track = subject.track
    return mutant

# FUNCTION THAT CHECKS IF TARGET CITY IS ON BUSES TRACK
def check(aim, track):
    for i in range(len(track)):
        if track[i] == aim:
            logical = True
            break
        else:
            logical = False
    return logical