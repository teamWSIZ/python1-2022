data = [(5,'Adam'), (3,'Jane'), (5, 'Xiao'), (2,'Jane')]

d = {}

for id, name in data:
    if name not in d:
        d[name] = [id]
    else:
        d[name].append(id)

for name, ids in d.items():
    if len(ids) > 1:
<<<<<<< HEAD
        print(f"Dla imienia {name} występuje więcej niż jednego id: {ids}")
=======
        print(f"Dla imienia {name} występuje więcej niż jednego id: {ids}")
>>>>>>> c860fc8678d2a9d3f9133f8b49d626a6b2a2c3b1
