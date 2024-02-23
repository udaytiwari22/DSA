from QueueUsing_LL import QueueLL

s = QueueLL()
s.enqueue(1)
s.enqueue(9)
s.enqueue(3)
s.enqueue(4)
s.enqueue(7)
while s.isEmpty() is False:
    print(s.dequeue())

print(s.front())
