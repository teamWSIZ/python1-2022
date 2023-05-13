data = [(5,'Adam'), (3,'Jane'), (5, 'Xiao'), (2,'Jane')]

d = {}

for id, name in data:
    if name not in d:
        d[name] = [id]
    else:
        d[name].append(id)

for name, ids in d.items():
    if len(ids) > 1:
        print(f"Dla imienia {name} występuje więcej niż jednego id: {ids}")