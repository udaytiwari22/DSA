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
        if head == None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = tail.next
    return head


def printLL(head):
    while head is not None:
        print(str(head.data)+"-->", end="")
        head = head.next
    print("None")
    return

def reverse_iteratively(head):
    curr=head
    prev=None
    while curr is not None:
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
    head=prev
    return head
    
        

head = takeInput()
printLL(head)
head=reverse_iteratively(head)
printLL(head)