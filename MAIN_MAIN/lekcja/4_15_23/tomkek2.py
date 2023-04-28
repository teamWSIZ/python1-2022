def isUnique(li):
    if len(li) <= len(set(li)): return True
    return False

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
    # for cul in lookForCulprit(SeenIds[1])[1]:
    #     print(cul)

    
        
        

print(NotUniqueIds(people))