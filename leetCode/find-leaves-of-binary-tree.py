'''as far as i got'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        print(str(root))

        latest_leaf_nodes = []
        stack = deque([])

        current_node = root

        while root != None:

            if (current_node.left == None) and (current_node.right == None):
                latest_leaf_nodes.append(current_node.val)
                leaf_val = current_node.val
                current_node = stack.pop()

            elif (current_node.left != None):
                stack.append(current_node)
                current_node = current_node.left
                continue

            elif (current_node.right != None):
                stack.append(current_node)
                current_node = current_node.right
                continue


# re-write answer in python tomorrow

if __name__ == "__main__" :
    print('hi')