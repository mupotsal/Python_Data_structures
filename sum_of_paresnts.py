class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def final(root,x):
    total = [0]
    sum_parents(root, x, total)
    return total[0]

def sum_parents(root,x, total):
    if not root:
        return 0

    if root:
        if (root.left and root.left.data == x )or (root.right and root.right.data == x):
             total[0] += root.data
    sum_parents(root.left, x, total)
    sum_parents(root.right, x, total)




def main():
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(7)
    root.left.right = Node(2)
    root.right.left = Node(2)
    root.right.right = Node(3)

    parents_sum = final(root, 2)
    print(parents_sum)

main()