# InOrder : Left-> Node -> Right
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def in_order(root):
    current = root
    s = []
    done = 0

    while(not done):
        if current is not None:
            # adding all the left nodes of the tree
            s.append(current)
            current = current.left
        else:
            if len(s) > 0:
                # get the last node from the stack
                current = s.pop()
                print(current.data)
                current = current.right
            else:
                done = 1

def morris_traversal(root):

    current = root

    while(current is not None):

        if current.left is None:
            print(current.data)
            current = current.right
        else:

            pre = current.left
            while(pre.right is not None and pre.right != current):
                pre = pre.right

            if pre.right is None:
                pre.right = current
                current = current.left
            else:
                pre.right = None
                print(current.data)
                current = current.right

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
#in_order(root)
morris_traversal(root)