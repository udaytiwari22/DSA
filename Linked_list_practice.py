class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def takeInput():
    inputList = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for currentdata in inputList:
        if currentdata == -1:
            break
        newNode = Node(currentdata)
        
        if head == None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode

    return head


def printLL(head):
    while head is not None:
        print(str(head.data), "-->", end="")
        head = head.next
    print("None")
    return


head = takeInput()
printLL(head)
