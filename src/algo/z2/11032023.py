import random

def listDividers(a, b):
    for i in range(len(a)):
        x = 0
        for j in range(len(b)):
            if b[j] % a[i] == 0:
                x += 1
        result.append(x)
    return result


def listGenerator():
    a = []
    b = []
    for i in range(4):
        x = random.randint(1,30)
        y = random.randint(1,30)
        a.append(x)
        b.append(y)
    
    return a, b

a, b = listGenerator()
print(f"Lista a to: {a} \nLista b to : {b}")
result = listDividers(a, b)
print(f"Wynik wynosi: {result}")
