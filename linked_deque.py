class DLNode:
    def __init__(self, previous_node = None, data_portion = None, next_node = None):
        self.previous = previous_node
        self.data = data_portion
        self.next = next_node

    def get_data(self):
        return self.data
    
    def set_data(self, new_data):
        self.data = new_data

    def get_next_node(self):
        return self.next
    
    def set_next_node(self):
        return self.next
    
    def set_next_node(self):
        self.next = next_node

    def get_previous_node(self):
        return self.previous
    
    def set_precious_node(self):
        self.previous = previous_node
    
class LinkedDeque:
    def __init__(self):
        self.front = None   # front
        self.back = None    # back
        self.size = 0       # tracker

    def add_to_back(self, new_entry):
        new_node = DLNode(None, new_entry, self.front)
        if self.is_empty():
            self.front = new_node
        else:
            self.back.set_previous_node(new_node)
        self.back = new_node
        self.size += 1
        

    def add_to_front(self, new_entry):
        new_node = DLNode(None, new_entry, self.front)
        if self.is_empty():
            self.back = new_node
        else:
            self.front.set_previous_node(new_node)
        self.front = new_node
        self.size += 1
        

    def get_back(self):
        if not self.is_empty():
            return self.back.get_data()
        else:
            raise IndexError("Deque is empty.")


    def get_front(self):
        if not self.is_empty():
            return self.front.get_data()
        else:
            raise IndexError("Deque is empty.")

    def remove_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty.")
        data = self.front.get_data()
        self.front = self.front.get_next_node()
        if self.front is not None:
            self.front.set_previous_node(None)
        else:
            self.back = None
        self.size -= 1
        return data

    def remove_back(self):
        if self.is_empty():
            raise IndexError("Deque is empty.")
        data = self.back.get_data()
        self.back = self.back.get_previous_node()
        if self.back is not None:
            self.back.set_next_node(None)
        else:
            self.front = None
        self.size -= 1
        return data     

    def clear(self):
        self.front = None
        self.back = None
        self.size = 0


    def is_empty(self):
        return self.size == 0

    def display(self):
        current = self.front
        elements = []
        while current is not None:
            elements.append(current.get_data())
            current = current.get_next_node()
        print("Deque contents:", elements)
