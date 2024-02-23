class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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
            while current.next != None:
                current = current.next
            current.next = newNode
    return head


def printLL(head):
    while head.next != None:
        print(str(head.data)+"->", end="")
        head = head.next
    print(None)
    return
def insertAtIR(head,i,data):
    if i<0:
        return head
    if i==0:
        newNode=Node(data)
        newNode.next=head
        return newNode
    if head==None:
        return None

    smallhead=insertAtIR(head.next,i-1,data)   
    head.next=smallhead
    return head     

s = takeInput()
printLL(s)
s=insertAtIR(s,3,23)
printLL(s)

