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

    def get_node(self, index):
        cur = self.head
        cur_idx = 0
        while cur_idx != index:
            cur = cur.next
            cur_idx += 1

        return cur.data


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(23)
linked_list.get_node(2) # -> 5를 들고 있는 노드를 반환해야 합니다!
print(linked_list.get_node(0))