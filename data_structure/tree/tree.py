from __future__ import print_function

class Node(object):
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)


def preorder(node):
    if not node:
        return
    print(node.data)
    preorder(node.left)
    preorder(node.right)


def max_depth(node):
    if not node:
        return 0

    l_depth = max_depth(node.left)
    r_depth = max_depth(node.right)
    if l_depth > r_depth:
        return l_depth + 1
    else:
        return r_depth + 1


def inorder(node):
    current = node
    stack = []
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif(stack):
            current = stack.pop()
            print(current.data)
            current = current.right
        else:
            break

def levelOrder(node):
    current = node
    stack = []

    stack.append(current)
    while stack:
        current = stack.pop(0)
        if current:
            print(current.data, end=' ')
            stack.append(current.left)
            stack.append(current.right)


def swapEveryLevel(root, level, k):
    # refer to  https://www.geeksforgeeks.org/swap-nodes-binary-tree-every-kth-level/
    if root is None or root.left is None or root.right is None:
        return
    if (level + 1) % k == 0:
        root.left, root.right = root.right, root.left

    swapEveryLevel(root.left, level+1, k)
    swapEveryLevel(root.right, level+1, k)


swapEveryLevel(root, 1, 2)

