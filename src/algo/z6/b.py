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