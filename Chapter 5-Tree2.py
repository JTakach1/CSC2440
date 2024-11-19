class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, value):
    if root is None:
        return Node(value)
    else:
        if value < root.val:
            root.left = insert(root.left, value)
        else:
            root.right = insert(root.right, value)
    return root

def sumDiv(root):
    if root is None:
        return 0
    sum_left = sumDiv(root.left)
    sum_right = sumDiv(root.right)
    if root.val % 5 == 0:
        currentVal = root.val
    else:
        currentVal = 0
    return sum_left + sum_right + currentVal

def print_inorder(root):
    if root:
        print_inorder(root.left)
        print(root.val, end=" ")
        print_inorder(root.right)

root = None
while True:
    value = input("Enter tree values (type 'done' when finished):")
    if value.lower() == 'done':
        break
        value = int(value)
        root = insert(root, value)

sum_div_5 = sumDiv(root)
print("Sum of nodes divisible by 5: " + str(sum_div_5))
("In-order traversal of the tree:")
print_inorder(root)
