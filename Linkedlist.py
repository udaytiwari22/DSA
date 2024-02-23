class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def printLL(head):
    while head is not None:
        print(str(head.data)+"-->", end="")
        head = head.next
    print("None")
    return


def takeInput():
    inputList = [int(ele) for ele in input().split()]
    head = None
    for currentData in inputList:
        if currentData == -1:
            break
        newNode = Node(currentData)
        if head is None:
            head = newNode
        else:
            current = head
            while current.next is not None:
                current = current.next
            current.next = newNode
    return head


head = takeInput()
print(head)
printLL(head)
