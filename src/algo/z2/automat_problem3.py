from random import seed, randint

from automat import run_tests, visualize


def best_multiply(a: list[int]) -> int:
    max = 0
    tmp =[]
    for i in range (0, len(a)):
        for j in range(i,len(a)):
            if a[i]*a[j] > max:
                max = a[i]*a[j]
                tmp = a[i],a[j]
                
    return f"{tmp} ma najwiekszy iloczyn rowny: {max}"


def generate_data(data_size):
 
    mx_num = 10 ** 4
    data_a = [randint(0, mx_num) for _ in range(data_size)]
    return {"a": data_a}


if __name__ == '__main__':
    x, y = run_tests(generate_data, best_multiply, max_size=10**4)
    visualize(x, y)