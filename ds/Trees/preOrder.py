# PreOrder : Node-> Left -> Right
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def iterative_pre_order(root):
    current = root
    if current:
        s = []
        s.append(root)

        while len(s) > 0:
            node = s.pop()
            print(node.data)

            if node.right is not None:
                s.append(node.right)
            if node.left is not None:
                s.append(node.left)

def recursive_pre_order(root):
    s = []
    if root:
        s.append(root.data)
        s = s + recursive_pre_order(root.left)
        s = s + recursive_pre_order(root.right)
    return s

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
#iterative_pre_order(root)
recursive_pre_order(root)
