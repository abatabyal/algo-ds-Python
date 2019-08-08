class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Left -> Root -> Right
def inorder(temp):
    if (not temp):
        return

    inorder(temp.left)
    print(temp.val, end= ",")
    inorder(temp.right)

# Root -> Left -> Right
def preorder(temp):
    if (not temp):
        return

    print(temp.val, end=",")
    preorder(temp.left)
    preorder(temp.right)

# Left -> Right -> Root
def postorder(temp):
    if (not temp):
        return

    postorder(temp.left)
    postorder(temp.right)
    print(temp.val, end=",")

root = Node(10)
root.left = Node(11)
root.left.left = Node(7)
root.right = Node(9)
root.right.left = Node(15)
root.right.right = Node(8)


print("Inorder traversal before insertion:", end = " ")
inorder(root)
print('\r')
preorder(root)
print('\r')
postorder(root)