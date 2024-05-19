from avltree import *

def calc_sum(node):
    if not node:
        return 0
    return node.key + calc_sum(node.right) + calc_sum(node.left)

# Driver program to test the above functions
root = None
keys = [10, 20, 30, 25, 28, 27, -1]

for key in keys:
    root = insert(root, key)

print("AVL-Дерево:")
print(root)
print(f"Summ of all values: {calc_sum(root)}")
