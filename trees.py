# Preorder Traversal (Root -> Left -> Right)
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)
# Inorder Traversal (Left -> Root -> Right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
# Postorder Traversal (Left -> Right -> Root)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")
# Take input
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right =None
    def insert(data,root):
        if(root is None):
            return Node(data)
        if root.data<data:
            root.right=Node.insert(data,root.right)
        elif(root.data>data):
            root.left=Node.insert(data,root.left)
        return root 
arr = list(map(int, input("Enter elements: ").split()))
root = None
for num in arr:
    root = Node.insert(num,root)

print("Preorder:")
preorder(root)

print("\nInorder:")
inorder(root)

print("\nPostorder:")
postorder(root)

