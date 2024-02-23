from QueueUsing_Array import QueueUsingArray

q=QueueUsingArray()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
while q.isEmpty() is False:
    print(q.front())
    print(q.dequeue())
    
    