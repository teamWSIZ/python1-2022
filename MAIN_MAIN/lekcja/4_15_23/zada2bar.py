data = (5,'Adam'), (3,'Jane'), (5, 'Xiao'), (2,'Jane')

print(data)

def id_filter(data):
    for x in data:

        id1 ,name = x
        duplicated_id = []
        print(id1)
        y = 2
        for y in range(len(data)):

            id2, name2 = data[y]
            print(id2)
            if id1 == id2:
                duplicated_id.append(id2)

    return duplicated_id


print(id_filter(data))
