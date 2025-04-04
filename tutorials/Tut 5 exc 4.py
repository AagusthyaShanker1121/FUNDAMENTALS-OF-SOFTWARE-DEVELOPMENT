import random as rand

def gen_rand(n):
    x = []
    for i in range(n):
        x.append(rand.randint(0, 10))
    return x

def factorial(n):
    return 1 if n in [1, 0] else n * factorial(n - 1)

def find_factorials(x):
    output = []
    for i in range(len(x)):
        output.append(factorial(x[i]))
    return output
    
def show():
    x = gen_rand(5)
    print(x)
    print(f"Factorials: {find_factorials(x)}")

show()