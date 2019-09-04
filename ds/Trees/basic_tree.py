class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def height(temp):
    if temp is None:
        return 0
    else:
        lheight = height(temp.left)
        rheight = height(temp.right)

        if lheight > rheight:
            return lheight + 1
        else:
            return  rheight + 1

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

def curr_level_nodes(root, level):
    if root is None:
        return
    if level == 1:
        print(root.val, end=",")
    elif level > 1:
        curr_level_nodes(root.left, level-1)
        curr_level_nodes(root.right, level-1)

def level_order_recursive(temp):
   h = height(temp)
   for i in range(1, h + 1):
       curr_level_nodes(temp, i)

def level_order(root):
    if root is None:
        return
    queue = []
    queue.append(root)

    while(len(queue) > 0):
        print(queue[0].val, end=",")
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def leaf_count(temp):
    if root is None:
        return 0
    q = []
    q.append(root)
    leaf_count = 0
    while (len(q) > 0):
        if q[0].right is None and q[0].left is None:
            leaf_count += 1
        node = q.pop(0)

        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)
    return leaf_count
root = Node(10)
root.left = Node(30)
root.right = Node(15)
print(leaf_count(root))