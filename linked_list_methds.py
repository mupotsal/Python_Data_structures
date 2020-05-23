# Linked List implementation

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

    def length(self, head):
        # think of edge cases
        temp = head
        num = 0
        while temp:
            num += 1
            temp = temp.next
        print(num)

    def search(self, head, target):
        temp = head
        num = 0
        while temp:
            if temp.data == target:
                return ("Yes found at", num)
            else:
                temp = temp.next
                num += 1
        return target, " is not found "

    def search_repetition(self,head, target):
        # this function tells how many times a given  number appears in the linked list
        temp = head
        appear = 0
        while temp:
            if temp.data == target:
                appear +=1
            temp = temp.next
        return "The number", target,"appeared ", appear, "times"



def main():

    myNode = Node(1)
    my_list = Linked_list()
    my_list.head = myNode
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)
    sev = Node(7)
    eight = Node(8)
    nine = Node(9)
    ten = Node(10)
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
    print(my_list.search_repetition(myNode,7))


main()

# find