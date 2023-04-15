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
    return True

print(isUnique([2,2,3,5,6,7]))
print(lookForCulprit([2,2,3,3,5,6,7]))