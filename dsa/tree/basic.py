class Tree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    def insert(self,root,value):
        if root == None:
            return Tree(value)
        if root.value < value:
            root.left = self.insert(root.left,value)
        else:
            root.right = self.insert(root.right,value)
        
        return root
    def display(self, root):
        if root is not None:
            print(root.value)
            self.display(root.left)
            self.display(root.right)
            
b = BinaryTree()
b.root = b.insert(b.root, 10)  # Insert the root node
b.root = b.insert(b.root, 9)    # Insert other nodes
b.root = b.insert(b.root, 8)
b.root = b.insert(b.root, 11)
b.root = b.insert(b.root,12)

b.display(b.root)  # This will display the tree