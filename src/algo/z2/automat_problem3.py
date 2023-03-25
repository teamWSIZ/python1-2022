from random import seed, randint

from automat import run_tests, visualize

dict ={}

def best_multiply(a: list[int]) -> int:
    max = 0
    tmp =[]
    for i in range (0, len(a)):
        for j in range(i,len(a)):
            if a[i]*a[j] > max:
                max = a[i]*a[j]
                tmp = a[i],a[j]
                
    return f"{tmp} ma najwiekszy iloczyn rowny: {max}"


#generator liczb losowych oparty na słowniku
def generate_data(data_size):
    data_list = []
    for _ in range(data_size*2):
        data_list.append(randint(1,100))
        dict['a'] = data_list[::2]
        dict['b'] = data_list[1::2]
    return {"a": dict.get('a')}



if __name__ == '__main__':
    x, y = run_tests(generate_data, best_multiply, max_size=10**4)
    visualize(x, y)