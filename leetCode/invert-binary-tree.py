'''
Given the root of a binary tree, invert the tree, and return its root.

'''
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flipNode(self, node: TreeNode):
        if node == None:
            return
            
        tmpLeft = node.left
        tmpRight = node.right
        # flip
        node.left = tmpRight
        node.right = tmpLeft

        if node.left != None:
            self.flipNode(node.left)
        
        if node.right != None:
            self.flipNode(node.right)


    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.flipNode(root)
        return root

if __name__ == "__main__":
    print('got this!!')
    sol = Solution()
    root = TreeNode(4)
    nodeTwo = TreeNode(2)
    nodeOne = TreeNode(1)
    nodeThree = TreeNode(3)
    nodeSeven = TreeNode(7)
    nodeSix = TreeNode(6)
    nodeNine = TreeNode(9)

    root.left = nodeTwo
    nodeTwo.left = nodeOne
    nodeTwo.right = nodeThree

    root.right = nodeSeven
    nodeSeven.left = nodeSix
    nodeSeven.right = nodeNine

    rtn = sol.invertTree(root)

    print(rtn)