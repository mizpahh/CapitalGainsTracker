class StockPurchase:
    def __init__(self, stock_symbol, cost_per_share, shares):
        self.stock_symbol = stock_symbol
        self.cost_per_share = cost_per_share
        self.shares = shares

    def __str__(self):
        return f"{self.stock_symbol}: ${self.cost_per_share} ({self.shares} shares)"