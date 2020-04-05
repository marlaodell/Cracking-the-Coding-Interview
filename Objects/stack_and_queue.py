class Holder:

    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return self.items == []

class Stack(Holder):

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        return self.items[len(self) - 1]

class Queue(Holder):

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        return self.items[0]