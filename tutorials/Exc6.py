def exc6():
    # Exercise 6:
    # Develop a program called Lab4Exc6 to achieve the following operations:
    # • Generate a random number of seed 10, n times (n is entered from keyboard).
    # • Then add only the even values
    # • Show the total of even values
    import random as rand

    n = int(input("Enter n: "))

    x = []
    total = 0
    for i in range(n):
        x.append(rand.randint(0, 100))
        print(x)

    for j in x:
        if j % 2 == 0:
            print(f"j is even so total += x {total} += {j}")
            total += j
            print(f"total = {total}")
def exc7():
    #   Read characters from keyboard until dot (.) is entered
    # • Count the number of vowels entered
    # • Uppercase and Lowercase vowels should be counted
    # • Display the total vowel count
    # NOTE:
    # • The program stops when . Is entered from keyboard
    vowels = ['a', 'o', 'e', 'i', 'u', 'y']
    x = input("Enter characters: ")
    print("\n Enter '.' to stop.")
    while '.' not in x:
        count = 0
        for i in range(len(x)):
            if x[i] in vowels:
                count += 1
                print(f"input[i] '{x[i]}' is a vowel, incrementing count.")
                print(f"Count: {count}")
        x = input("Enter characters: ")
def exc10():
    n = int(input("Enter number: "))
    fib, next, last = 1
    for i in range(n):
        next += last
          
        print(next)

exc10()
# 1, 1, 2, 3, 5