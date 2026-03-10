from enum import nonmember


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self,value):
        self.head = Node(value)

    # LinkedList 의 가장 끝에 있는 노드에 새로운 노드를 연결
    def append(self, value):
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)

    # LinkedList에서 저장한 head를 따라가면서 현재 있는 노드들을 전부 출력
    def print_all(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

linkedList = LinkedList(1)
print(linkedList.head.data)
linkedList.append(2)
print(linkedList.head.next.data)
linkedList.append(3)
print(linkedList.head.next.next.data)

linkedList.print_all()