from linked_deque import LinkedDeque
from stock_ledger import StockLedger

class LedgerEntry:
    def __init__(self, stock_symbol):
        self.stock_symbol = stock_symbol
        self.purchases = LinkedDeque() # Deque for storing StockPurchase objects
    
    def add_purchase(self, new_purchase):
        self.purchases.add_to_back(new_purchase)

    def remove_purchase(self):
        return self.purchases.remove_front() if not self.purchases.is_empty() else None
    
    def equals(self, other):
        return self.stock_symbol == other.stock_symbol
    
    def display_entry(self):
        print(f"{self.stock_symbol}: ", end="")
        current_node = self.purchases.front # starts from the front of the deque
        purchase_list = []
        
        while current_node is not None:
            purchase = current_node.get_data()
            purchase_list.append(f"{purchase.cost_per_share} ({purchase.shares} shares)")
            current_node = current_node.get_next_node()

    # join purchases into a single string & print
        print(", ".join(purchase_list))