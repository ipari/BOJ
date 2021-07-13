import sys


class Node:
    value = None
    left = None
    right = None

    def __init__(self, value):
        self.value = value

    def update(self, left, right):
        self.left = left
        self.right = right


N = int(sys.stdin.readline())

nodes = {}
root_int = ord('A')
for i in range(N):
    v = chr(root_int + i)
    nodes[v] = Node(v)

for i in range(N):
    v, left, right = map(str, sys.stdin.readline().split())
    nodes[v].update(nodes.get(left, None), nodes.get(right, None))


root_node = nodes['A']
preorder = []
inorder = []
postorder = []


def preorder_traversal(node):
    if node is None:
        return
    preorder.append(node.value)
    preorder_traversal(node.left)
    preorder_traversal(node.right)


def inorder_traversal(node):
    if node is None:
        return
    inorder_traversal(node.left)
    inorder.append(node.value)
    inorder_traversal(node.right)


def postorder_traversal(node):
    if node is None:
        return
    postorder_traversal(node.left)
    postorder_traversal(node.right)
    postorder.append(node.value)


preorder_traversal(root_node)
inorder_traversal(root_node)
postorder_traversal(root_node)

print(''.join(preorder))
print(''.join(inorder))
print(''.join(postorder))
