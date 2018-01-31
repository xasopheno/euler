class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def max_tree_depth(root):
    print('min_tree_depth()', root.key)
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    # If left subtree is Null, recur for right subtree
    if root.left is None:
        return max_tree_depth(root.right) + 1

    # If right subtree is Null , recur for left subtree
    if root.right is None:
        return max_tree_depth(root.left) + 1

    return max(max_tree_depth(root.left), max_tree_depth(root.right)) + 1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.left.right.left.left = Node(7)

print(max_tree_depth(root))
