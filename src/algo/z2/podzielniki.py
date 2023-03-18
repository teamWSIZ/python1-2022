from random import seed, randint

from automat import run_tests, visualize


def solve(a: list[int], b: list[int]) -> list[int]:
    result = []    
    for i in range (len(a)):
        counter = 0
        for j in range (len(b)):
            if b[j]%a[i]==0: counter+=1
        result.append(counter)
    return result


def generate_data(data_size):
    data_list = []
    for _ in range(data_size*2):
        data_list.append(randint(1,100))
        a = list(set(data_list[::2]))
        b = list(set(data_list[1::2]))
    return {"a": a, "b": b}

if __name__ == '__main__':
    x, y = run_tests(generate_data, solve, max_size=10**4)
    visualize(x, y)
    # print(solve([2, 5, 7, 9, 