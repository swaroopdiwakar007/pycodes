class Stack:
    def __init__(self):
        self.item = []

    def length(self):
        return len(self.item)

    def is_empty(self):
        return not self.item

    def insert(self, data):
        self.item.append(data)

    def pop(self):
        self.item.pop()

    def top(self):
        return self.item[0]

    def print_stack(self):
        print(self.item)

    def insert_list(self, ldata):
        self.item.extend(ldata)

# s = Stack()

# s.insert(2)
# s.insert(5)
# s.insert(9)
# s.insert_list([1,2,3])

# s.print_stack()

# s.pop()

# s.print_stack()
