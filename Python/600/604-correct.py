class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_height_balanced(root):
    if root is None:
        return True

    # Calculate the height of the left and right subtrees
    left_height = get_height(root.left)
    right_height = get_height(root.right)

    # Check if the absolute difference between the heights is not more than 1
    if abs(left_height - right_height) > 1:
        return False

    # Recursively check if both subtrees are height-balanced
    return is_height_balanced(root.left) and is_height_balanced(root.right)

def get_height(node):
    if node is None:
        return 0
    else:
        return 1 + max(get_height(node.left), get_height(node.right))