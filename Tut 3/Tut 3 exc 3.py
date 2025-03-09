import math

radius = float(input("Enter circle radius: "))
circle_area = math.pi * (radius ** 2)
print(f"Circle area of radius: {circle_area:.3f}")
volume = (4/3) * math.pi * (radius ** 3)
print(f"Sphere volume of radius: {volume}")
