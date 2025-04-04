# Develop a program called Lab4Exc5 to achieve the following operations:
# • Add all even numbers from 1 up to n and prints the total, where the value of n is entered from keyboard.
# • The program should print the even-sum of every entered n
# NOTE:
# • The program stops when -1 is entered from keyboard.


n = int(input("Enter n: "))

while n != -1:
    x = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            print(f"Adding {i} to {x}")
            x += i
            print(f"x = {x}")
    n = int(input("Enter n: "))
