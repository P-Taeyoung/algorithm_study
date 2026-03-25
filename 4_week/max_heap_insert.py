# Q. 맥스 힙은 원소를 추가한 다음에도 맥스 힙의 규칙을 유지해야 한다.
# 맥스 힙에 원소를 추가하시오.
class MaxHeap:
    def __init__(self):
        self.items = [None]

    # 내 풀이
    # 삽입된 인덱스에서 //2를 통해 부모 인덱스 구함.
    # 부모 인덱스에 해당되는 값과 비교하여 더 큰 경우에 자리를 바꿔줌
    def insert_1(self, value):
        # 구현해보세요!
        self.items.append(value) # 먼저 맨 뒤에 값을 삽입
        current_idx = len(self.items) - 1

        if current_idx <= 1:
            return self.items

        parent_idx = current_idx // 2 #부모노드 구하기

        while parent_idx > 0 and self.items[current_idx] > self.items[parent_idx]: # 부모 노드와 비교하여 자식노드가 더 크지 않을때까지 반복
            self.items[parent_idx], self.items[current_idx] = self.items[current_idx], self.items[parent_idx] #부모와 자식 노드 자리 바꿈
            current_idx = parent_idx  #현재 노드를 전 부모노드로 이동
            parent_idx = current_idx // 2 #이에 따라 부모 노드를 다시 지정

        return self.items[1:]


max_heap = MaxHeap()
max_heap.insert_1(3)
max_heap.insert_1(4)
max_heap.insert_1(2)
print(max_heap.insert_1(9))
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!