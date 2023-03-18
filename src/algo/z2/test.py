def largest_sum_10_percent(a: list[int]) -> int:
    size = int(len(a)/10)
    max = 0
    for x in range (0,int(len(a)/2)):
        b = sum(a[(x*size):((size*x+1)+1)])
        if b > max: max = b
    return max

a = [5,6,1,1,1,1,1,1,1,1,5,8,1,1,1,1,1,1,1,1]
print(largest_sum_10_percent(a))