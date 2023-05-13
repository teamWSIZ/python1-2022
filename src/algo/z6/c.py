def repeat(list):
<<<<<<< HEAD
  #lista unikatowych id
  repeated = []
  for y in range (len(list)+1):
    repeated.append([y,0])
  #sprawdzenie powtorzen id
=======
  ################################# lista unikatowych id
  repeated = []
  for y in range (len(list)+1):
    repeated.append([y,0])
  ################################# sprawdzenie powtorzen id
>>>>>>> c860fc8678d2a9d3f9133f8b49d626a6b2a2c3b1
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
<<<<<<< HEAD
      print("dla id=",z," pojawiaja sie ",repeated[z][1]," rozne imiona")
=======
      print("dla id= ",z," pojawiaja sie " ,repeated[z][1], " rozne imiona")
>>>>>>> c860fc8678d2a9d3f9133f8b49d626a6b2a2c3b1
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
<<<<<<< HEAD
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
=======
>>>>>>> c860fc8678d2a9d3f9133f8b49d626a6b2a2c3b1
