# binary search tree - pre order traversal

class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# static
def getPreIndex():
    return constructTreeUtil.preIndex

# static
def incrementPreIndex():
    constructTreeUtil.preIndex += 1

def constructTreeUtil(pre, low, high):

    # base case
    if (low > high):
        return None

    root = Node(pre[getPreIndex()])
    incrementPreIndex()


    if low == high:
        return root

    r_root = -1

    for i in range(low, high+1):
        if (pre[i] > root.data):
            r_root = i
            break

    if r_root == -1:
        r_root = getPreIndex() + (high - low)

    root.left = constructTreeUtil(pre, getPreIndex(), r_root-1)

    root.right = constructTreeUtil(pre, r_root, high)

    return root

def constructTree(pre):
    size = len(pre)
    constructTreeUtil.preIndex = 0
    return constructTreeUtil(pre, 0, size-1)

def printInOrder(root):
    if root is None:
        return
    printInOrder(root.left)
    print(root.data, end=' ')
    printInOrder(root.right)

if __name__ == '__main__':
    pre = [10, 5, 1, 7, 40, 50]

    root = constructTree(pre)

    printInOrder(root)