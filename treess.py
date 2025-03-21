# Recursive Python program for level order traversal of Binary Tree

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

# Helper function for recursive level order traversal
def levelOrderRec(root, level, res):
    if not root:
        return

    # Add a new level to the result if needed
    if len(res) <= level:
        res.append([])

    # Add current node's data to its corresponding level
    res[level].append(root.data)

    # Recur for left and right children
    levelOrderRec(root.left, level + 1, res)
    levelOrderRec(root.right, level + 1, res)

# Function to perform level order traversal
def levelOrder(root):
    res = []
    levelOrderRec(root, 0, res)
    return res
      
if __name__ == "__main__":
    # Create binary tree
      #      1         
    #     / \       
    #    3   2      
    #          \   
    #           4 
    #          /  \
    #         6    5
    root = Node(1)
    root.left = Node(3)
    root.right = Node(2)
    root.right.right = Node(4)
    root.right.right.left = Node(6)
    root.right.right.right = Node(5)

    # Perform level order traversal
    res = levelOrder(root)

    # Print the result
    for level in res:
        for data in level:
            print(data, end=" ")

