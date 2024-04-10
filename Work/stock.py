class Stock:
    def __init__(self, name, shares, price):
        self.name = str(name)
        self.shares = int(shares)
        self.price = float(price)

    def cost(self):
        return self.shares * self.price

    def sell(self, num):
        self.shares -= num

class MyStock(Stock):
    def panic(self):
        self.sell(self.shares)

    def cost(self):
        actual_cost = super().cost()
        return 1.25 * actual_cost
