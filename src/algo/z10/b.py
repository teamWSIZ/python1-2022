def relative_list(a: list[int], b: str) -> bool:
    j = 0
    for i in b:
        if i == "<":
            if j == len(a) - 1 or a[j] >= a[j + 1]:
                return False
        elif i == ">":
            if j == len(a) - 1 or a[j] <= a[j + 1]:
                return False
        else:
            return False
        j += 1
    return True