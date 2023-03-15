from datetime import datetime
import matplotlib.pyplot as plt
from random import seed, randint


def generate_data(data_size):
    data_list = []
    for _ in range(data_size*2):
        data_list.append(randint(1,100))
    return data_list

def solve_problem(data):
    result = []
#Wersja list
    # a, b = data[::2], data[1::2]
#Wersja set
    a = list(set(data[::2]))
    b = list(set(data[1::2]))
    for i in range (len(a)):
        counter = 0
        for j in range (len(b)):
            if b[j]%a[i]==0: counter+=1
        result.append(counter)
    return result


def run_tests(generator, solver):
    size = 10
    sizes = []
    times = []
    while size < 1000:
        print(f'testing solver for {size=}')
        data = generator(size)
        REPETITIONS = 400
        time_sum = 0
        for i in range(REPETITIONS):
            st = datetime.now().timestamp()
            ret = solver(data)
            en = datetime.now().timestamp()
            time_sum += (en - st)

        sizes.append(size)
        times.append(time_sum / REPETITIONS * 10 ** 6)
        size *= 2

    return sizes, times


if __name__ == '__main__':
    x, y = run_tests(generate_data, solve_problem)

    plt.plot(x, y)
    plt.xlabel("Rozmiar danych")
    plt.ylabel("Czas wykonania (usec)")
    plt.show()
