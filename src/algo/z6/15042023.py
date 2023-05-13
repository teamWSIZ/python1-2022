def unique(list1):
  unique_list = []
  for x in list1:
    if x in unique_list:
      print("Lista nieunikalna")
      return
    if x not in unique_list:
      unique_list.append(x)
  print("Lista unikalna")
list1 = ['aa', 'a', 'c', 'bb', 'bb']
print(list1)
unique(list1)

list2 = ['aa', 'a', 'c', 'bb',]
print(list2)
unique(list2)

def unique(list1):
  unique_list = []
  repeated_list = []
  for x in list1:
    if x in unique_list:
      if x not in repeated_list:
        repeated_list.append(x)
    if x not in unique_list:
      unique_list.append(x)
  if len(repeated_list) > 0:
    print("Lista nieunikalna, powtórzone elementy: " , repeated_list)
  else:
    print("Lista unikalna")

#tests
list1 = ['aa', 'a', 'c', 'bb',]

def repeat(list):
  #lista unikatowych id
  repeated = []
  for y in range (len(list)+1):
    repeated.append([y,0])
  #sprawdzenie powtorzen id
  #print(repeated)
  x = [list[i][0] for i in range (len(list))]
  for i in range (len(x)):
    if (x[i] in x[:i]) or (x[i] in x[i+1:]): 
      #print (x[i], i)
      id = x[i]
      #print(repeated[id])
      repeated[id][1] = repeated[id][1] +1
  #print(repeated)
  for z in range (len(list)+1):
    if repeated[z][1] > 0:
      print("dla id=",z," pojawiaja sie ",repeated[z][1]," rozne imiona")
  count = 0
  for zz in range (len(list)+1):
    if repeated[zz][1] > 0:
      count = count+1
  if count == 0:
    print("Kazdy posiada  swoje unikatowe id")


#tests
list1 = [(5,'Adam'), (3,'Jane'), (1, 'Xiao'), (2,'Jane'), (6,'Jane')]
print(list1)
repeat(list1)

list2 = [(5,'Adam'), (3,'Jane'), (5, 'Xiao'), (2,'Jane'), (3,'Jane'),(5,'Adam'), (3,'Jane'), (5, 'Xiao'), (2,'Jane'), (3,'Jane')]
print(list2)
repeat(list2)
print(list1)
unique(list1)

list2 = ['aa', 'a', 'c', 'bb', 'bb']
print(list2)
unique(list2)

list3 = ['aa', 'a', 'c', 'bb', 'bb', 'bb']
print(list3)
unique(list3)

list4 = ['aa', 'a', 'c', 'bb', 'bb', 'a']
print(list4)
unique(list4)


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
