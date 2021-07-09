#Program to insert in a BST

class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key

def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.val==key:
            return root
        elif root.val<key:
            root.right=insert(root.right,key)
        else:
            root.left=insert(root.left,key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

r = Node(50)
r = insert(r, 35)
r = insert(r, 20)
r = insert(r, 47)
r = insert(r, 79)
r = insert(r, 62)
r = insert(r, 17)
 
# Print inoder traversal of the BST
inorder(r)
