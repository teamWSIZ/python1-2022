# const
dt = 0.001
g = 10
MAX_THRUST = 20

# vars
s = 0
v = 0
t = 0


thrust = MAX_THRUST * 0.80
mass = 100

# g == gravity
# a == acceleration
# t = time
# v = velocity
# s = distance

#  s = a * t ** 2 / 2
#  v = a * t
#


# symulacja
while t < 20:
    acc = (thrust / mass) - g
    mass -= thrust * 0.01 * dt
    s += v * dt
    v += acc * dt
    t += dt
    print(f'{s}')

print(s)
print(g * t ** 2 / 2)
