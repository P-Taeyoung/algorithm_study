class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        # 어떻게 하면 될까요?
        if self.is_empty():
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return

    def dequeue(self):
        # 어떻게 하면 될까요?
        if self.is_empty():
            print("Queue is empty")
            return None
        else:
            delete_head = self.head
            self.head = self.head.next
        return delete_head.data

    def peek(self):
        # 어떻게 하면 될까요?
        if self.is_empty():
            print("Queue is empty")
            return None
        else:
            return self.head.data


    def is_empty(self):
        # 어떻게 하면 될까요?
        if self.head is None:
            return True
        return False

queue_1 = Queue()
queue_1.enqueue(1)
print(queue_1.peek())
queue_1.enqueue(2)
print(queue_1.peek())
queue_1.enqueue(3)
print(queue_1.peek())
print(queue_1.dequeue())
print(queue_1.peek())
print(queue_1.dequeue())
print(queue_1.peek())
print(queue_1.dequeue())
print(queue_1.peek())