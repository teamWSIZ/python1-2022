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

def split_data(data):
    print(data)
    x, y = [], []

    for i in range(len(data)):
        if i%2 == 0:
            x.append(data[i])
        else:
            y.append(data[i])

    return x,y

print(split_data(dane))

dane2a = [2,5,7,9]
dane2b = [4,8,18,27]

def filter_data(dane2a, dane2b):
    output = []
    for x in range(len(dane2b)):
        print(x)
        number = dane2b[x]/dane2a[x]
        print(number)
        if number%2 == 0:
            output.append(number)
    return output

print(filter_data(dane2a, dane2b))