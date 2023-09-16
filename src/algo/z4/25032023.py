"""
zadanie1:
 Mając dany "rozkład jazdy (z pliku gen_train_data.py), wyświetlić miasto z którego jest najwięcej 
 połączeń wychodzących.

""" 
import collections 
from trains.gen_train_data import generate_data


def get_city_most_connections(train_data: list[tuple[int,int]]) -> int:
    x = []
    for i in range(len(train_data)):
        x.append(train_data[i][0])
    counteredNumbers = collections.Counter(x)
    y = max(counteredNumbers, key=counteredNumbers.get)
    return y

train_data = generate_data(10)
print(train_data)
print("Z miasta o numerze "+str(get_city_most_connections(train_data))+" jest najwięcej połączeń wychodzących.")
