class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def takeInput():
    inputList = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for currentData in inputList:
        if currentData == -1:
            break
        newNode = Node(currentData)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = tail.next  # tail=newNode , can also be written here
    return head


def printLL(head):
    while head is not None:
        print(str(head.data)+"-->", end="")
        head = head.next
    print("None")
    return


def reverseR(head):
    if head == None or head.next == None:
        return head

    smallhead = reverseR(head.next)
    curr = smallhead
    while curr.next is not None:
        curr = curr.next
    curr.next = head
    head.next = None
    return smallhead


def reverse2(head):
    if head == None or head.next == None:
        return head, head
    smallhead, smalltail = reverse2(head.next)
    smalltail.next = head
    head.next = None
    return smallhead, head


def reverse3(head):
    if head == None or head.next == None:
        return head
    smallhead = reverse3(head.next)
    tail = head.next
    tail.next = head
    head.next = None
    return smallhead


head = takeInput()
printLL(head)
# head, tail = reverse2(head)
# printLL(head)
head = reverse3(head)
printLL(head)