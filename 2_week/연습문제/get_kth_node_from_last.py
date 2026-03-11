# Q. 링크드 리스트의 끝에서 K번째 값을 반환하시오.
# [6] -> [7] -> [8] # 이런 링크드 리스트가 입력되었을 때,
#                   # 끝에서 2번째 값은 7을 반환해야 합니다!

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
    # 내풀이
    # 연결리스트의 총길이를 알아낸 이후에 K번째 값 출력
    def get_kth_node_from_last_1(self, k):
        # 구현해보세요!
        list_length = 0
        cur = self.head
        while cur is not None:  # 연결리스트 총길이 구하기
            list_length += 1
            cur = cur.next

        answer_idx = list_length - k # K번째 값을 구하기 위한 Index 값

        count = 0
        cur = self.head
        while count < answer_idx:
            cur = cur.next
            count += 1

        return cur

    #강의_개선안
    #탐색을 k 만큼의 구간을 두고 중복 탐색함.
    # slow탐색 -- k 구간 --  fast 탐색
    # [1] -> [2] -> [3] -> [4]
    # fast 탐색이 끝에 다 달았을 때 slow 탐색 노드가 정답이 됨.
    def get_kth_node_from_last_2(self, k):
        fast_cur = self.head
        slow_cur = self.head
        count = 0
        while fast_cur is not None:
            if count == k:
                slow_cur = slow_cur.next
            else:
                count += 1
            fast_cur = fast_cur.next

        return slow_cur

linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)
linked_list.append(9)

print(linked_list.get_kth_node_from_last_1(2).data)  # 7이 나와야 합니다!
print(linked_list.get_kth_node_from_last_2(2).data)  # 7이 나와야 합니다!