class Node:

    def __init__(self, data = None):
        self.next = None
        self.prev = None
        self.data = data

class CircularLinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)

        