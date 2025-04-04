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
        return self.list


n = Numbers()

n.populate(20)
n.show()
n.clear()
n.populate(5)
n.show()