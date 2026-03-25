# Q. 맥스 힙은 원소를 제거한 다음에도 맥스 힙의 규칙을 유지해야 한다.
# 맥스 힙의 원소를 제거하시오.
class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

    def delete_1(self):
        # 구현해보세요!
        # 루프노드와 맨 끝 노드 바꾸기
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        deleted_node = self.items.pop() # 맨 끝 노드 삭제
        cur_idx = 1
        while cur_idx < len(self.items) - 1:
            left_child_idx = 2 * cur_idx
            right_child_idx = 2 * cur_idx + 1
            left_is_bigger = left_child_idx < len(self.items) and self.items[left_child_idx] > self.items[cur_idx]
            right_is_bigger = right_child_idx < len(self.items) and self.items[right_child_idx] > self.items[cur_idx]

            if left_is_bigger and right_is_bigger: # 두 자식노드 모두 크다면
                if self.items[left_child_idx] > self.items[right_child_idx]: # 둘 중 더 큰 노드와 바꾸기
                    self.items[cur_idx], self.items[left_child_idx] = self.items[left_child_idx], self.items[cur_idx]
                    cur_idx = left_child_idx
                else:
                    self.items[cur_idx], self.items[right_child_idx] = self.items[right_child_idx], self.items[cur_idx]
                    cur_idx = right_child_idx
            elif left_is_bigger: # 왼쪽 자식노드가 크다면
                self.items[cur_idx], self.items[left_child_idx] = self.items[left_child_idx], self.items[cur_idx]
                cur_idx = left_child_idx
            elif right_is_bigger: # 오른쪽 자식노드가 크다면
                self.items[cur_idx], self.items[right_child_idx] = self.items[right_child_idx], self.items[cur_idx]
                cur_idx = right_child_idx
            else: # 둘 다 작다면
                break

        return deleted_node  # 8 을 반환해야 합니다.
    #강의안 풀이
    #현재 인덱스와 현재인덱스 포함 자식 인덱스(2개) 중 가장 큰 값을 가진 인덱스와 자리를 바꿔줌
    def delete_2(self):
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        deleted_node = self.items.pop()

        cur_idx = 1
        while cur_idx < len(self.items) - 1:
            max_idx = cur_idx
            right_child_idx = 2 * cur_idx + 1
            left_child_idx = 2 * cur_idx

            if left_child_idx < len(self.items) - 1 and self.items[left_child_idx] > self.items[max_idx]:
                max_idx = left_child_idx
            if right_child_idx < len(self.items) - 1 and self.items[right_child_idx] > self.items[max_idx]:
                max_idx = right_child_idx
            if cur_idx == max_idx:
                break

            self.items[cur_idx], self.items[max_idx] = self.items[max_idx], self.items[cur_idx]
            cur_idx = max_idx

max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 6, 7, 2, 5, 4]
print(max_heap.delete_1())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 6, 4, 2, 5]

max_heap2 = MaxHeap()
max_heap2.insert(8)
max_heap2.insert(6)
max_heap2.insert(7)
max_heap2.insert(2)
max_heap2.insert(5)
max_heap2.insert(4)
print(max_heap2.items)  # [None, 8, 6, 7, 2, 5, 4]
print(max_heap2.delete_2())  # 8 을 반환해야 합니다!
print(max_heap2.items)  # [None, 7, 6, 4, 2, 5]