def get_min_number_of_operations(a: list[int]) -> int:
    count = 0
    length = len(a)
    end = 0
    while length > end:
        if a[end] < 0:
            count = count +1
            while a[end] <= 0:
                   end = end+1
                   if length == end: break
        end = end +1
    return count

print(get_min_number_of_operations([1, 0, -1, -1, 0, 2, -2, -2, -2]))