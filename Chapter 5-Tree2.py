class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def input_tree_values():
    root = None
    print("Enter the values to insert into the BST, separated by spaces:")
    values_input = input("Enter values: ")
    values = values_input.split()

    for value in values:
        if value.isdigit() or (value[0] == '-' and value[1:].isdigit()):  # Check for negative numbers as well
            root = insert(root, int(value))
        else:
            print("Non digit in input, removing it.")
    return root

def sum_of_divisible_by_5(root):
    if root is None:
        return 0
    sum_div_5 = 0
    if root.val % 5 == 0:
        sum_div_5 += root.val
    sum_div_5 += sum_of_divisible_by_5(root.left)
    sum_div_5 += sum_of_divisible_by_5(root.right)

    return sum_div_5

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)

if __name__ == "__main__":
    root = input_tree_values()
    sum_div_5 = sum_of_divisible_by_5(root)
    print(f"Sum of values divisible by 5: ", sum_div_5)
    print("In-order traversal of the tree:")
    inorder_traversal(root)
    print()
