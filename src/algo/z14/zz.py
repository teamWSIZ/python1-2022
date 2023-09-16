d = 0b0000

# set bit "2" to 1
# d |= (1 << 2)
# print(bin(d))

# set bit "1" to 0
print(bin(d))
d = (~(1 << 3)) & d
print(bin(d))
