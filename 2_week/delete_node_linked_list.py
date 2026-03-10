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

        return cur

    def add_node(self, index, data):
        new_node = Node(data)
        #index값이 0일 때 예외처리
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            prev_node = self.get_node(index - 1)
            tmp_node = prev_node.next
            prev_node.next = new_node
            new_node.next = tmp_node

    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
        else:
            self.get_node(index - 1).next = self.get_node(index + 1)







linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(23)
linked_list.print_all()
linked_list.delete_node(2)
linked_list.print_all()