from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return Node(val)
    queue = deque([root])
    while queue:
        temp = queue.popleft()
        if temp.left is None:
            temp.left = Node(val)
            break
        else:
            queue.append(temp.left)
        if temp.right is None:
            temp.right = Node(val)
            break
        else:
            queue.append(temp.right)
    return root

def sum_div(root):
    if root is None:
        return 0

    sum_left = sum_div(root.left)
    sum_right = sum_div(root.right)
    if root.data % 5 == 0:
        current_val = root.data
    else:
        current_val = 0

    return sum_left + sum_right + current_val

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)

def inputTreeValues():
    root = None
    while True:
        value = input("Enter tree values (type 'done' when finished): ")
        if value.lower() == 'done':
            break
        value = int(value)
        root = insert(root, value)
    return root

root = inputTreeValues()
sum_div_5 = sum_div(root)
print("Sum of nodes divisible by 5:", sum_div_5)
print("In-order traversal of the tree:")
inorder(root)
