from avltree import *

def find_biggest(root):
    if not root:
        return None
    curr = root
    while curr.right:
        curr = curr.right
    return curr.key

# Driver program to test the above functions
root = None
keys = [10, 20, 30, 25, 28, 27, -1]

for key in keys:
    root = insert(root, key)

print("AVL-Дерево:")
print(root)
print(f"Biggest value in tree: {find_biggest(root)}")

