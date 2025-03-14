# • Repeat-print out n stars on one line (where the value of n is captured from keyboard).
# NOTES:
# • Don't forget to terminate the previous line.
# • The program should terminate when n is zero.

n = int(input("Enter number of stars: "))

s = ""
for i in range(n):
    s += "*"
print(s)