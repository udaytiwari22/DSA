class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

a=Node(23)
b=Node(32)
a.next=b
print(a.data)
print(b.data)
print(a.next.data)
print(a.next)
print(b)        
print(b.next.data)