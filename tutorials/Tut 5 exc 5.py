def get_inpt():
    inpt = int(input("Enter size of diamond (-1 to stop): "))
    return inpt

def print_dmds(n):
    for i in range(1, n+1):
        print(f"{" " * (n - i)}{"* " * i}{" " * (n - i)}")
    for i in range(n-1, 0, -1):
        print(f"{" " * (n - i)}{"* " * i}{" " * (n - i)}")
range
def get_factorial(x):
    return 1 if x in [1,0] else x * get_factorial(x - 1)

# inpt = get_inpt()
inpt = 5
while inpt != -1:
    print_dmds(inpt)
    inpt = get_inpt()