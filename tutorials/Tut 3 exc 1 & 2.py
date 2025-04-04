
x = 4
y = 2
print(f"Excercise 1: \n\n")
print(f"x + y = {(x + y):.3f}")
print(f"x - y = {(x - y):.3f}")
print(f"x / y = {x / y:.3f}")
print(f"x * y = {(x * y):.3f}")
print(f"x % y + x / y = {(x % y + x / y):.3f}")
result = ((y**7 + 7 / (5**0.5 + x)) * ((x**4 % 5) + 2))
print(f"((y**7 + 7) / (5**0.5 + x)) * (x**4 % 5 + 2) = {((y**7 + 7) / (5**0.5 + x)) * (x**4 % 5 + 2):.3f}")
print(f"Excercise 1 Complete... \n\n")

x = int(input("Enter value for x: "))
y = int(input("Enter value for y: "))

z = x ** y
print(f"z = x ** y, z = {z:.3f}")
result = z ** 0.5
print(f"Square root of z = {result}")
