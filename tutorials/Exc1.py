
# Display all numbers from 1 to 10
# • Display the square roots of each number
# • Display the exponents of each number
# • Show all displays in a tabular format (refer to lecture 4)

def print_separator():
    print("-"*table_width)

table_width = 34
columns = ['Number', 'Sqrt', 'Exp']
n = 10

print_separator()
s = ""
for curr_col in columns:
    s += "|" + f"{curr_col}".center(10)
print(s)
print_separator()

for i in range(1, n+1):
    s = "".join(["|", f"{i}".center(10)])
    s += "".join(["|", f"{i ** 0.5:2f}".center(10)])
    s += "".join(["|", f"{i ** 2}".center(10)])
    s += "|"
    print(s)
    


print_separator()
