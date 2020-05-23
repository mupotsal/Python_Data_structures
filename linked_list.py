
#Linked List implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None

    def traversal(self, head):
        temp = head
        while temp:
            print(temp.data)
            temp = temp.next

    def length(self,head):
        # think of edge cases
        temp = head
        num = 0
        while temp:
            num += 1
            temp = temp.next
        print(num)

    def search(self,head,target):
        temp = head
        num = 0
        while temp:
            if temp.data == target:
                return ("Yes found at", num)
            else:
                temp = temp.next
                num += 1
        return target, " is not found "


def main():
    newNode = Node("Liberty")
    linked_list = Linked_list()
    linked_list.head = newNode
    second = Node("Saffa")
    third = Node("Umu")
    linked_list.head.next = third
    third.next = second
    linked_list.traversal(newNode)
    linked_list.length(newNode)
    print(linked_list.search(newNode,"Umu"))
    
    myNode = Node(1)
    my_list = Linked_list()
    my_list.head = myNode
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)
    sev =Node(7)
    eight = Node(8)
    nine = Node(9)
    ten= Node(10)
    myNode.next = two
    two.next = three
    three.next = four
    four.next = five
    five.next = six
    six.next = sev
    sev.next = seven
    seven.next = eight
    eight.next = nine
    nine.next = ten


main()

# find