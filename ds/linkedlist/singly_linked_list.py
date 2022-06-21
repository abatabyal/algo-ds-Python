class Node:

    def __init__(self, data=None):
        self.next = None
        self.data = data


class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            print('Previous Node does not exist')
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node
        new_node.next = None

    def printlist(self):
        temp = self.head
        while (temp):
            if temp != self.head:
                print('--->', end='')
            print(f'{temp.data}', end='')
            temp = temp.next
        print('\r')

    def middle_element(self):
        temp = self.head
        list_len = 0
        while (temp):
            list_len += 1
            temp = temp.next
        mid_index = list_len // 2

        temp = self.head
        for i in range(mid_index):
            temp = temp.next
        return temp.data

    def get_len(self):
        temp = self.head
        list_len = 0
        while temp:
            list_len += 1
            temp = temp.next
        return list_len

    def get_nth_from_end(self, n):
        list_len = self.get_len()
        if n == list_len:
            return self.head.data
        temp = self.head
        for i in range(list_len - n):
            nth_last = temp.next
            temp = temp.next
        return nth_last.data

    def rotate(self, n):
        list_len = self.get_len()
        if n == list_len:
            return self.head.data
        new_head = self.head
        new_tail = None
        for i in range(n):
            if i == n - 1:
                new_tail = new_head
            new_head = new_head.next
        curr_last_node = self.head
        while (curr_last_node.next != None):
            curr_last_node = curr_last_node.next
        new_tail.next = None
        curr_last_node.next = self.head
        self.head = new_head

    def detect_loop_hashing(self):
        s = set()
        temp = self.head
        while (temp):
            if temp in s:
                return True
            s.add(temp)
            temp = temp.next
        return False

    def detect_loop_floyd(self):
        slow_p = self.head
        fast_p = self.head
        while (slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                print("Found Loop")
                return


# s_list = SinglyLinkedList()
# s_list.head = Node(1)
# second = Node(2)
# third = Node(3)
# s_list.head.next = second
# second.next = third
# s_list.printlist()
# s_list.push(4)
# s_list.printlist()
# s_list.insert_after(s_list.head.next,5)
# s_list.printlist()
# s_list.append(6)
# s_list.printlist()
# print(s_list.middle_element())
# print(s_list.get_nth_from_end(6))
# s_list.rotate(3)
# s_list.printlist()
# s_list.push(10)
# s_list.push(4)
# s_list.push(15)
# s_list.push(20)
# s_list.push(50)
#
# # Create a loop for testing
# s_list.head.next.next.next.next.next = s_list.head
#
# if (s_list.detect_loop_hashing()):
#     print("Loop found")
# else:
#     print("No Loop ")
# s_list.detect_loop_floyd()
