from random import randint, seed

N_CITIES = 20
# seed(111)

current_map = [(1,2), (2,4), (4,3), (3,1), (3, 5), (5, 1)]

def generate_data(data_size):
    res = []
    for i in range(data_size):
        res.append((randint(0, N_CITIES - 1), randint(0, N_CITIES - 1)))
    return res


def nextStop(start_point, train_map):

    hmm_dest = []
    
    for el in train_map:
        if el[0] == start_point:
            print("sooo trueee")
            hmm_dest.append(el[1])

    return hmm_dest

def thinkAgentThink(possibilities):
    print("SO MANY POSSIBILITIES ", possibilities)
    return possibilities[randint(0, len(possibilities)-1)]


def iGoByTrain(name, map, where_istart, cycles):
    
    possible_dest = nextStop(where_istart, map)
    if len(possible_dest) > 1:
        possible_dest = thinkAgentThink(possible_dest)
    print("I", name, "am going to ", possible_dest)
    while cycles > 0:
        cycles -= 1
        iGoByTrain(name, map, possible_dest[0], cycles)


print(iGoByTrain("john", current_map, 1, 4))


    


