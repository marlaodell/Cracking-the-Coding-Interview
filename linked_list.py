from trees_and_nodes import Node

class LinkedListNode(Node):

    def __init__(self, val, next=None):
        Node.__init__(self, val)
        self.next = next

    def __eq__(self, other):
        return Node.__eq__(self, other) and self.next == other.next

class LinkedList():

    def __init__(self, head = None):
        self.head = head
        self.length = 0

    def __str__(self):
        string =  ""
        pointer = self.head
        while pointer:
            string += str(pointer.val) + " => "
            pointer = pointer.next
        return string[: -4] #Take off last arrow

    def __len__(self):
        return self.length

    def __eq__(self, other):
        pointer1 = self.head 
        pointer2 = other.head
        while pointer1 and pointer2:
            if pointer1 != pointer2:
                return False
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return True

    def add_front(self, val):
        holder = self.head
        self.head = LinkedListNode(val, holder)

    def add_back(self, val):
        if not self.head:
            self.head = LinkedListNode(val)
        else:
            x = self.head
            while x.next: #Find last element in the LinkedList
                x = x.next
            x.next = LinkedListNode(val)
        self.length += 1

def build_linked_list(values):
    ll = LinkedList()
    for i in values:
        ll.add_back(i)
    return ll