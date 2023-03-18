from random import seed, randint

from automat import run_tests, visualize


def largest_sum_10_percent(a: list[int]) -> int:
    size = int(len(a)/10)
    max = 0
    for x in range (0,int(len(a)/2)):
        b = sum(a[(x*size):((size*x+1)+1)])
        if b > max: max = b
    return max


def generate_data(data_size):
    seed(111)
    mx_num = 10 ** 4
    data_a = [randint(0, mx_num) for _ in range(data_size)]
    return {"a": data_a}


if __name__ == '__main__':
    x, y = run_tests(generate_data, largest_sum_10_percent, max_size=10**4)
    visualize(x, y)
    # print(solve([2, 5, 7, 9, 2], [4, 8, 18, 