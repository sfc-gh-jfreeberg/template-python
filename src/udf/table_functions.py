class CostByCategory_TF:
    def __init__(self):
        self._sum = 0
        self._category = ""

    def process(self, category, quantity, price):
        self._category = category
        cost = quantity * price
        self._cost_total += cost
        yield (category, cost)

    def end_partition(self):
        yield (self._category, self._cost_total)
