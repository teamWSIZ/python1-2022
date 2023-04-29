# A

def isUnique(li):
    if len(li) <= len(set(li)): return True
    return False

# B

def lookForCulprit(li):
    blames = set()
    for el in li:
        if li.count(el) > 1: blames.add(el)
    if len(blames) == 0:
        return False

    print("blame",blames)
    return True, blames


# print(isUnique([2,2,3,5,6,7]))
# print(lookForCulprit([2,2,3,3,5,6,7]))

people = [[1, "Jane"], [2, "Jane"], [2, "Amon"], [3, "James"], [2, "Anit"], [2, "Amir"]]

def NotUniqueIds(li):
    Culprit = []
    PrevEl = [0]
    for elem in li:
        print(elem[0])
        if elem[0] == PrevEl[0]:
            Culprit.append([elem, PrevEl])
            
        PrevEl = elem
        print(PrevEl)
        print(Culprit)
        

print(NotUniqueIds(people))


# C i D

def id_exists(lista):
    for x in range(len(lista)):
        id = lista[x][0]
        for y in range(x+1, len(lista)):
            if id == lista[y][0]:
                return True
    return False


lista = [(5,'Adam'), (3,'Jane'), (5, 'Xiao'), (2,'Jane')]

print(id_exists(lista))

