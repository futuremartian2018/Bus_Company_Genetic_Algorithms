# CLASS THAT REPRESENTS CITIES EXISTING ON THE MAP
class Town:
    pass

# CLASS THAT REPRESENTS PASSENGERS
class Passg:
    pass

# CLASS THAT REPRESENTS CITY CONNECTIONS
class Conect:
    pass

# CLASS THAT REPRESENTS PARENTS - BUS COMPANIES
class Parent:

    def __init__(self):
        self.cost = 0
        self.take = 0
        self.gain = 0
        self.happy = 0
        self.fitness = 0
        self.fleet = []
    
# CLASS BUS THAT REPRESENTS BUSES TRAVELLING ACROSS THE MAP
class Bus:

    def __init__(self, start, seats, length):
        self.start = start
        self.seats = seats
        self.length = length
        self.track = []
        self.cost = 0
        self.take = 0
        self.gain = 0
        self.happy = 0
        self.fitness = 0

# FUNCTION THAT SAVES BEST ROUTE
def track_map(bus):
    ind_x = []
    ind_y = []
    for i in range(len(bus.track) - 1):
        ind_x.append(bus.track[i])
        ind_y.append(bus.track[i + 1])
    return ind_x, ind_y



