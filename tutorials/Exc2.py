
# Generate 20 random integers
# Store the values into an array
# Display the array

import random

n = 20
x = []
for i in range(20):
    x.append(random.randint(0, 100))

print(x)