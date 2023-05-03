from random import seed, randint

from src.algo.z2.automat import run_tests, visualize


# Problem A 

def largest_sum_10_percent(a: list[int]) -> int:
 n = len(a)
 k = n // 10
 max_sum = float('-inf')
 for i in range(n-k+1):
 subarray_sum = sum(a[i:i+k])
 if subarray_sum > max_sum:
 max_sum = subarray_sum
 return max_sum

#B

def solve(a: list[int]) -> int:
   def generate(data_size):
    return {"a": [random.randint(0, 100) for _ in range(data_size)]}
    return 10


def generate_data(data_size):
    seed(111)
    mx_num = 10 ** 4
    data_a = [randint(0, mx_num) for _ in range(data_size)]
    return {"a": data_a}


if __name__ == '__main__':
    x, y = run_tests(generate_data, solve, max_size=10**4)
    visualize(x, y)
    # print(solve([2, 5, 7, 9, 2], [4, 8, 18, 27]))import random

def generate(data_size):
    return {"a": [random.randint(0, 100) for _ in range(data_size)]}

#C


def best_multiply(a: list[int]) -> int:
    if len(a) < 2:
        raise ValueError("List must contain at least two elements.")
    max1 = max(a)
    a.remove(max1)
    max2 = max(a) if a else max1
    return max1 * max2


def generate_data(data_size):
    seed(111)
    mx_num = 10 ** 4
    data_a = [randint(-mx_num, mx_num) for _ in range(data_size)]
    return {"a": data_a}


if __name__ == '__main__':
    x, y = run_tests(generate_data, best_multiply, max_size=10**4)
    visualize(x, y)
