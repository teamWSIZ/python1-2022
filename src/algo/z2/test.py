from random import seed, randint

from automat import run_tests, visualize


# def largest_sum_10_percent(a: list[int]) -> int:
#     size = int(len(a)/10)
#     max = 0
    
#     print (" ")
#     print (f"rozmiar: {size}")
    
#     print (" ")
#     for x in range (0,int(len(a)/size)):
#         b = a[(x*size):((size*x+size))]
#         print (b)
#         tmp = sum(b)
#         if tmp > max: 
#             max = tmp 
#             tab = b
#     print (" ")
#     return tab

# a = [1,1,1,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,2,3,1,1,1,1,2,1,1,1,1,1]
# print(largest_sum_10_percent(a))

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
    return data_a



for i in range (10,20):
    a = generate_data(i) 
    print (a)
    print(best_multiply(a))

