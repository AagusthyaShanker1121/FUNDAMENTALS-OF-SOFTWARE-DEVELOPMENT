import math

def calc_perim(r):
    perimeter = 2 * math.pi * r
    return perimeter

def calc_area(r):
    area = math.pi * (r ** 2)
    return area

def calc_volume(r):
    volume = (4/3) * (math.pi * (r ** 3))
    return volume

def show(r):
    print(f"\n\nCIRCLE STATS:\n \t Permieter: {calc_perim(r):3f} \n\t Area: {calc_area(r):3f} \n\t Volume: {calc_volume(r)}")

inpt = input("Enter radius: ")
inpt = float(inpt)

show(inpt)