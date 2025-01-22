import sys

class Node:

    def __init__(self, data = None):
        self.next = None
        self.prev = None
        self.data = data

class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):

        new_node = Node(new_data)

        new_node.next = self.head

        if self.head != None:
            self.head.prev = new_node

        self.head = new_node

    def insert_after(self, prev_node, new_data):

        if prev_node is None:
            return

        new_node = Node(new_data)

        new_node.next = prev_node.next

        prev_node.next = new_node

        new_node.prev = prev_node

        if new_node.next is not None:
            new_node.next.prev = new_node

    def append(self, new_data):

        new_node = Node(new_data)

        new_node.next = None

        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        last = self.head
        #traverse list
        while last.next != None:
            last = last.next

        last.next = new_node

        new_node.prev = last

        return

    def print_list(self, node):

        while node is not None:
            print(node.data)
            last = node
            node = node.next

    def length(self):
        i = 0
        head = self.head
        if self.head is None:
            return

        while head is not None:
            head = head.next
            i += 1

        return i

    def pop(self, index):

        if self.head is None:
            return

        node = self.head

        if index == 0:
            self.head = node.next
            node = None
            return

        for i in range(index - 1):
            node = node.next
            if node is None:
                break

        if node is None:
            return
        if node.next is None:
            return

        # Node temp.next is the node to be deleted
        # store pointer to the next of node to be deleted
        next = node.next.next

        node.next = None

        node.next = next

llist = DoublyLinkedList()

llist.append(6)
#llist.print_list(llist.head)
llist.push(7)
#llist.print_list(llist.head)
llist.push(1)
#llist.print_list(llist.head)
llist.append(4)
#llist.print_list(llist.head)
llist.insert_after(llist.head, 67)
llist.print_list(llist.head)
print("Length :" + str(llist.length()))
llist.pop(0)
llist.print_list(llist.head)

