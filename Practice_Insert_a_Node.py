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
            tail = tail.next
    return head


def insertAtI(head, i, data):
    count = 0
    prev = None
    curr = head
    newNodeI = Node(data)
    while count < i:
        prev = curr
        curr = curr.next
        count += 1
    if prev == None:
        head = newNodeI
        newNodeI.next = curr

    else:
        prev.next = newNodeI
        newNodeI.next = curr
    return head


def insertAtI_R(head, i, data):
    if i < 0:
        return head
    if i == 0:
        newNode = Node(data)
        newNode.next = head
        return newNode
    if head == None:
        return None

    smallhead = insertAtI_R(head.next, i-1, data)
    head.next = smallhead
    return head


def printll(head):
    while head != None:
        print(str(head.data)+"->", end="")
        head = head.next
    print("None")
    return


h = takeInput()
printll(h)
# h = insertAtI(h, 0, 4)
h = insertAtI_R(h, 3, 5)
printll(h)
