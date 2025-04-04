import random
import statistics

def gen_rand(n):
    x = []
    for i in range(n):
        x.append(random.randint(0, 100))
    return x

def calc_mean(x):
    y = 0
    for i in range(len(x)):
        y += x[i]
    mean = y / len(x)
    return mean

def calc_std(x, mean):
    diff = 0
    for i in range(len(x)):
        diff += (x[i] - mean) ** 2
    std_dev = (diff / (len(x)-1)) ** (1/2)
    return std_dev

def def_std(x):
    return statistics.stdev(x)

array = gen_rand(20)
mean = calc_mean(array)
mystdev = calc_std(array, mean)
act_std = def_std(array)

print(f"Array of rand ints: {array}")
print(f"Mean of array: {mean}")
print(f"My std dev calc: {mystdev}")
print(f"Act std dev: {act_std}")
