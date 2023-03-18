from datetime import datetime
import matplotlib.pyplot as plt
from random import seed, randint


def generate_data(data_size):
    # tutaj wstawić coś co generuje dane dla naszego algorytmu
    return [randint(0, 10 ** 6) for _ in range(data_size)]
    pass


def solve_problem(l1, l2):
    
    wyndziel = []
    for el1 in l1:
        dziel = 0  
        for el2 in l2:
            if el2 % el1 == 0:
                dziel += 1
                
        wyndziel.append(dziel)
    
    return wyndziel


def run_tests(generator, solver):
    size = 10
    sizes = []
    times = []
    while size < 10000:
        print(f'testing solver for {size=}')
        data = generator(size)
        data1 = generator(size)
        REPETITIONS = 400
        time_sum = 0
        for i in range(REPETITIONS):
            st = datetime.now().timestamp()
            ret = solver(data, data1)
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
