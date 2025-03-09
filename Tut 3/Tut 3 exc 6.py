class Car:
    def __init__(self, make, pos):
        self.make = make
        self.pos = pos

    def move(self, distance):
        self.pos += distance
        return

    def __str__(self):
        return f"{self.make} is at position {self.pos}"
    

Mercedes = Car("Mercedes", 2)
print(Mercedes)

Mercedes.move(10)
print(Mercedes)