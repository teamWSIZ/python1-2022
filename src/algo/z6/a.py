def unique(list1):
  unique_list = []
  for x in list1:
    if x in unique_list:
      print("not unique")
      return
    if x not in unique_list:
      unique_list.append(x)
  print("unique")
list1 = ['aa', 'a', 'c', 'bb', 'bb']
print(list1)
unique(list1)

list2 = ['aa', 'a', 'c', 'bb',]
print(list2)
unique(list2)
