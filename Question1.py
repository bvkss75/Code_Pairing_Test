class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_maximum_value(node):
    if node is None:
        return float('-inf')
    
    left_max = find_maximum_value(node.left)
    right_max = find_maximum_value(node.right)
    
    return max(node.value, left_max, right_max)

def calculate_tree_depth(node):
    if node is None:
        return 0
    
    left_depth = calculate_tree_depth(node.left)
    right_depth = calculate_tree_depth(node.right)
    
    return max(left_depth, right_depth) + 1

def build_tree():
    value = input("Enter the node value (or type 'None' to skip): ")
    
    if value.lower() == 'none':
        return None
    
    node = BinaryTreeNode(int(value))
    print(f"Enter left child of {value}:")
    node.left = build_tree()
    print(f"Enter right child of {value}:")
    node.right = build_tree()
    
    return node

root = build_tree()

if root:
    max_value = find_maximum_value(root)
    tree_depth = calculate_tree_depth(root)
    
    print(f"Maximum value in the tree: {max_value}")
    print(f"Depth of the tree: {tree_depth}")
else:
    print("The tree is empty.")
