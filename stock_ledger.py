#from ledger_entry import LedgerEntry
from stock_purchase import StockPurchase
from linked_deque import LinkedDeque

class StockLedger:
    def __init__(self):
        self.entries = LinkedDeque() # store LedgerEntry onjects

    def display_ledger(self):
        print("---- Stock Ledger ----")
        current_node = self.entries.front
        while current_node is not None:
            entry = current_node.get_data()
            entry.display_entry()               # Display purchases for each stock
            current_node = current_node.get_next_node()

    
    def get_entry(self, stock_symbol):
        current_node = self.entries.front
        while current_node is not None:
            entry = current_node.get_data()
            if entry.equals(LedgerEntry(stock_symbol)):
                return entry
            current_node = current_node.get_next_node()
        return None
    

    def buy(self, stock_symbol, shares_bought, price_per_share):
        # entry for stock symbol alr exisits?
        entry = self.get_entry(stock_symbol)

        if entry is None:
            entry = LedgerEntry(stock_symbol)
            self.entries.add_to_back(entry)

        new_purchase = StockPurchase(stock_symbol, price_per_share, shares_bought)
        entry.add_purchase(new_purchase)


    def sell(self, stock_symbol, shares_sold, price_per_share):
        entry = self.get_entry(stock_symbol)

        if entry is None:
            print(f"No entries for {stock_symbol}. Cannot sell.")
            return

        total_cost = 0
        total_shares_sold = 0
        while shares_sold > 0 and not entry.purchases.is_empty():
            purchase = entry.remove_purchase() #FIFO

            if purchase.shares > shares_sold:

                total_cost += shares_sold * purchase.cost_per_share
                total_shares_sold += shares_sold
                purchase.shares -= shares_sold

                entry.add_purchase(purchase) # add it back

                shares_sold = 0
            
            else:
                total_cost += purchase.shares * purchase.cost_per_share     # sell all shares from purchase
                total_shares_sold += purchase.shares
                shares_sold -= purchase.shares                              # decrease num shares shold

            profit_or_loss = (price_per_share * total_shares_sold) - total_cost
            print(f"Sold {total_shares_sold} shares of {stock_symbol} at ${price_per_share} each.")
            print(f"Total cost basis: ${total_cost}, Profit/Loss: ${profit_or_loss}")

        # def display_ledger(self):
        #     print("---- Stock Ledger ----")
        #     current_node = self.entries.front
        #     while current_node is not None:
        #         entry = current_node.get_data()
        #         entry.display_entry()               # Display purchases for each stock
        #         current_node = current_node.get_next_node()

        
        # def get_entry(self, stock_symbol):
        #     while current_node is not None:
        #         entry = current_node.get_data()
        #         if entry.equals(LedgerEntry(stock_symbol)):
        #             return entry
        #         current_node = current_node.get_next_node()
        #     return None

            