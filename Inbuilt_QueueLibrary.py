import queue

# inbuilt Queue

# s=queue.Queue()
# s.put(2)
# s.put(4)
# s.put(7)
# s.put(9)
# while  not s.empty():
#     print(s.get())


s = queue.LifoQueue()
s.put(2)
s.put(4)
s.put(7)
s.put(9)
while not s.empty():
    print(s.get())
