import random

class Numbers:
    def __init__(self):
        print("Numbers created.")
        self.list = []

    def populate(self, n):
        if self.list != []:
            return "List already full"
        x = []
        for i in range(n):
            x.append(random.randint(0, 100))
        self.list = x
        print(f"List populated: {self.list}")
        return None

    def clear(self):
        self.list = []
        print(f"List Emptied, List: {self.list}")
        return None
    
    def show(self):
        print(self.list)
        return None
    
    def number(self, tgt):
        for i in range(len(self.list)):
            if tgt == self.list[i]:
                return i
            return -1
    
    def find(self, tgt):
        loc = self.number(tgt)
        if loc != -1:
            print(f"Number found: {tgt} at index {loc}")
        else:
            print("Target does not exist")

    def numbers(self, tgts: list[int]):
        x = []
        for i in range(len(self.list)):
            if self.list[i] in tgts:
                x.append(i)
        if len(x) > 0:
            return x
        else:
            return -1
        
    def findAll(self, tgts: list[int]):
        found = self.numbers(tgts)
        if found != -1:
            print(f"Numbers found at indexes {found}")
        else:
            print("Target does not exist")

    def delete(self, tgt):
        for i in range(len(self.list)):
            if self.list[i] == tgt:
                print(f"Deleting {tgt} @ index: {i}.")
                self.list.pop(i)
    
    def update(self, val, idx):
        if abs(idx) > len(self.list)-1:
            print(f"Index too high, i: {idx}, list length: {len(self.list)}")
            return None
        self.list[idx] = val
        print(f"Value ({val}) inserted @ index {i}")

class Menu:
    def __init__(self):
        self.n = Numbers()
    
    def __main__(self):
        inpt = input("Enter operation to execute (p/c/f/F/d/u/x):")
        while inpt != "x":
            match inpt:
                case "p":
                    length = input("Enter length to populate: ")
                    self.n.populate(length)
                case "c":
                    self.n.clear()
                case "f":
                    tgt = input("Enter number to find: ")
                    self.n.find(tgt)
                case "F":
                    tgt = input("Enter numbers to find sep by ,: ")
                    self.n.find(tgt)
            

targets = [random.randint(0, 100) for _ in range(20)]
print(f"Targets: {targets}")
