
class Pay:
    def __init__(self, name, amount):
        self.name = name
        self. amount = amount

    def deposit(self, dep):
        if dep < 0:
            return self.amount
        self.amount += dep
        return self.amount

    def withdrawal(self, amount):
        if amount > self.amount:
            return "withdrawal not success"
        self.amount -= amount

