
def is_unique(a:list[str]) -> bool:
    return list(set(a)) == list(a)

def get_duplicates(a:list[str]) -> list:
    duplicates = []
    for val in a:
        if a.count(val) > 1 and val not in duplicates:
            duplicates.append(val)
            return duplicates

if __name__ == '__main__':
    lst = ['aa', 'a', 'c', 'bb', 'ab', 'aa']
    print(is_unique(lst))
    print(get_duplicates(lst))
