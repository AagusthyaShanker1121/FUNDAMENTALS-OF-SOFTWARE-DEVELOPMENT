import random

x = random.randint(1, int(1e6-1))
x = str(x)

print(len(x))

while len(x) < 6:
    x = "0" + x