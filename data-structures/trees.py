# data structure - binary tree
# https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    # insert node
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    
    # print tree
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data), # what is with colon?
        if self.right:
            self.right.printTree()

    # inorder traversal
    # left -> root -> right
    def inorderTraversal(self,root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

    # preorder traversal
    # root -> left -> right
    def PreorderTraversal(self,root):
        ret = []
        if root:
            ret.append(root.data)
            ret = ret + self.PreorderTraversal(root.left)
            ret = ret + self.PreorderTraversal(root.right)
        return ret

    # post order traversal
    # left -> right -> root
    def postorderTraversal(self,root):
        res = []
        if root:
            res = self.postorderTraversal(root.left)
            res = res + self.postorderTraversal(root.right)
            res.append(root.data)
        return res

if __name__ == "__main__":
    root = Node(27)
    #root.printTree()
    root.insert(14)
    root.insert(35)
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)
    print(root.postorderTraversal(root))
