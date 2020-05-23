class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if not root:
        return
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def post_order(root):
    if not root:
        return
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.data, end = " ")

def sum_nodes(root, total):
    if root == None:
        return 0
    if root:
        total[0] += root.data
    sum_nodes(root.left, total)
    sum_nodes(root.right, total)

def thesum(root):
    total = [0]
    sum_nodes(root, total)
    return total[0]

def addBT(root):
    if (root == None):
        return 0
    return (root.data + addBT(root.left) + addBT(root.right))

def main():
    root = Node(10)
    root.left = Node(9)
    root.right = Node(8)
    root.left.left = Node(7)
    root.left.right = Node(6)
    root.right.left = Node(5)
    root.right.right = Node(4)
    root.left.left.left = Node(3)
    root.left.left.right = Node(2)
    root.left.right.left = Node(1)

    # inorder(root)
    print(" ")
    # post_order(root)
    print(" ")
    final = thesum(root)
    total = addBT(root)
    print(total)
    print()
    print(final)

main()


