
def is_uniqe(a: list[tuple[int, str]]) -> bool:
    ids = set(row[0] for row in a)
    names = set(row[1] for row in a)
    if len(ids) == len(a) and len(names) == len(a):
        return True
    else:
        return False


def get_repeated(a: list[tuple[int, str]]) -> list[str] or None:
    check_id = []
    check_name = []
    names = []
    ids = []
    for id_, name in a:
        check_name.append(name)
        check_id.append(id_)
        if check_name.count(name) > 1:
            names.append(name)
        if check_id.count(id_) > 1:
            ids.append(id_)

    if len(ids) >= 1 or len(names) >= 1:
        return print(
            f"dla id={ids} pojawiają się różne names, dla name={names} pojawiają się różne id's"
        )
    else:
        return print("Wartości są unikatowe")



if __name__ == '__main__':
    lst = [(5,'Adam'), (3,'Jane'), (5, 'Xiao'), (2,'Jane')]
    lst2 = [(1,'Adam'), (2,'Jane'), (3, 'Xiao'), (4,'Jade')]
    print(is_uniqe(lst))
    print(is_uniqe(lst2))
    get_repeated(lst)
    get_repeated(lst2)
