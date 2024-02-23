class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def lengthofLL(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count


def insertAtI(head, i, data):
    if i < 0 or i > lengthofLL(head):
        return head
    count = 0
    prev = None
    current = head
    while count < i:
        prev = current
        current = current.next
        count += 1
    newNode = Node(data)
    if prev is not None:
        prev.next = newNode
    else:
        head = newNode
    newNode.next = current
    return head


def takeInput():
    inputList = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for currentdata in inputList:
        if currentdata == -1:
            break
        newNode = Node(currentdata)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = tail.next

    return head


def printll(head):
    while head != None:
        print(str(head.data)+"->", end="")
        head = head.next
    print("None")
    return


j = takeInput()
print(lengthofLL(j))
printll(j)
j = insertAtI(j, 2, 10)
printll(j)
