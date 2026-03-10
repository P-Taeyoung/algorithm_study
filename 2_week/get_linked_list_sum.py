# Q.  다음과 같은 두 링크드 리스트를 입력받았을 때, 합산한 값을 반환하시오.
# 예를 들어 아래와 같은 링크드 리스트를 입력받았다면,
# 각각 678, 354 이므로 두개의 총합
# 678 + 354 = 1032 를 반환해야 한다.
# 단, 각 노드의 데이터는 한자리 수 숫자만 들어갈 수 있다.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def change_int(self):
        cur = self.head
        num = cur.data
        while cur.next is not None:
            num *= 10
            cur = cur.next
            num += cur.data
        return num

    def print_all(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

# 내풀이:
    # 먼저 각 노드에 있는 데이터를 구해 완전한 숫자로 만들기
    # 완전한 숫자끼리 더하기
    # 더한 값 자리 하나하나씩을 노드에 추가
def get_linked_list_sum_1(linked_list_1, linked_list_2):
    num_1 = linked_list_1.change_int()
    num_2 = linked_list_2.change_int()
    sum = str(num_1 + num_2) # 문자로 변환하여 쉽게 자리수별로 연결리스트에 추가할 수 있도록 함.
    answer_linked_list = LinkedList(int(sum[0]))
    for i in range(1, len(sum)):
        answer_linked_list.append(int(sum[i]))

    return answer_linked_list

linked_list_1 = LinkedList(7)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(1)
linked_list_2.append(4)

get_linked_list_sum_1(linked_list_1, linked_list_2).print_all()