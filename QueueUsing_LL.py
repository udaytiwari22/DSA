from NodeFor_Import import Node


class QueueLL:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    def enqueue(self, data):
        newNode = Node(data)
        if self.__head == None:
            self.__head = newNode
            self.__tail = newNode

        else:
            self.__tail.next = newNode
        self.__tail = newNode
        self.__count += 1

    def dequeue(self):
        if self.__head == None:
            print("Queue is Empty")
            return
        data = self.__head.data
        self.__head = self.__head.next
        self.__count = self.__count-1
        return data

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.size() == 0

    def front(self):
        if self.__head == None:
            print("Queue is Empty")
            return
        data = self.__head.data
        return data
