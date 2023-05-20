def repeat(list):
  ################################# lista unikatowych id
  repeated = []
  for y in range (len(list)+1):
    repeated.append([y,0])
  ################################# sprawdzenie powtorzen id
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
      print("dla id= ",z," pojawiaja sie " ,repeated[z][1], " rozne imiona")
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
