class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        # 어떻게 하면 될까요?
        cur = self.head
        self.head = Node(value)
        self.head.next = cur
        return

    # pop 기능 구현
    def pop(self):
        # 어떻게 하면 될까요?
        if self.is_empty():
            return "Stack is empty"
        popped = self.head
        self.head = self.head.next
        return popped

    def peek(self):
        # 어떻게 하면 될까요?
        if self.is_empty():
            return "Stack is empty"
        return self.head

    # isEmpty 기능 구현
    def is_empty(self):
        # 어떻게 하면 될까요?
        if self.head is None:
            return True
        else:
            return False

stack_1 = Stack()
stack_1.push(1)
stack_1.push(2)
stack_1.push(3)
print(stack_1.peek().data)
print(stack_1.pop().data)
print(stack_1.peek().data)
print(stack_1.pop().data)
print(stack_1.peek().data)
print(stack_1.is_empty())
print(stack_1.pop().data)
print(stack_1.is_empty())
print(stack_1.pop())
print(stack_1.is_empty())