import random

z = 0
f = 0
í = 0
while z != 1000000:
    x = random.randint(1, 2)
    if x == 1:
        f = f + 1
    if x == 2:
        í = í + 1
    z = z + 1
print("Fej: ", f, ' Írás: ', í)
