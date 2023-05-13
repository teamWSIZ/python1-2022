def unique(list1):
  unique_list = []
  for x in list1:
    if x in unique_list:
<<<<<<< HEAD
      print("Lista nieunikalna")
      return
    if x not in unique_list:
      unique_list.append(x)
  print("Lista unikalna")
=======
      print("not unique")
      return
    if x not in unique_list:
      unique_list.append(x)
  print("unique")
>>>>>>> c860fc8678d2a9d3f9133f8b49d626a6b2a2c3b1
list1 = ['aa', 'a', 'c', 'bb', 'bb']
print(list1)
unique(list1)

list2 = ['aa', 'a', 'c', 'bb',]
print(list2)
<<<<<<< HEAD
unique(list2)
=======
unique(list2)
>>>>>>> c860fc8678d2a9d3f9133f8b49d626a6b2a2c3b1
