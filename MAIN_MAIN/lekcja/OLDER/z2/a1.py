import matplotlib as mat

dane = [
    5, 0.7,
    10, 0.75,
    100, 2.4,
    200, 4.9,
    400, 11,
    800, 29,
    1600, 86,
    3200, 224,
    6400, 497,
    12800, 1092]

# zadanie -- wszystkie elementy na parzystych elementach --> do listy "x", pozostae do listy "y"

x, y = [], []

for i in range(len(dane)):
    if i % 2 == 0:
        x.append(dane[i])
    else:
        y.append(dane[i])

mat.print(x)
