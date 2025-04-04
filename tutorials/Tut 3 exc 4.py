
x1 = float(input("Please input the x1 cordinate of point A: "))
y1 = float(input("Please input the y1 cordinate of point A: "))

x2 = float(input("Please input the x2 cordinate of point B: "))
y2 = float(input("Please input the y2 cordinate of point B: "))

distance = (
    (x2 - x1) ** 2 + 
    (y2 - y1) ** 2  
) ** (1/2)

print(f"The distance between point A & B is: {distance}")