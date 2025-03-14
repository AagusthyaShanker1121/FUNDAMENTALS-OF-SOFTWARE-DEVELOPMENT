# Read n integers from keyboard.
# • Display the min and max values entered.
# NOTE:
# • The program ends when -1 is entered.

x = 0
a = []
print("Enter -1 to stop.")
while x != -1:
    x = int(input("Enter numbers: "))
    a.append(x)
    print(f"Min: {min(a)}, Max: {max(a)}")
    
