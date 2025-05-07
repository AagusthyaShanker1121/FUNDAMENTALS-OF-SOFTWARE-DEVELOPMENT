class Customer:
    def __init__(self, name):
        self.name = name
        print(f"Customer added: {name}")

    def add_bank(self, Bank):
        self.bank = Bank

    