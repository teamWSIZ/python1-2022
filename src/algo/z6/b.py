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
    print("not unique, repeated items: " , repeated_list)
  else:
    print("unique")

#tests
list1 = ['aa', 'a', 'c', 'bb',]
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
