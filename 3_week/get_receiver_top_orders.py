# Q. 수평 직선에 탑 N대를 세웠습니다. 모든 탑의 꼭대기에는 신호를 송/수신하는 장치를 설치했습니다.
# 발사한 신호는 신호를 보낸 탑보다 높은 탑에서만 수신합니다. 또한 ,한 번 수신된 신호는 다른 탑으로 송신되지 않습니다.
#
# 예를 들어 높이가 6, 9, 5, 7, 4 인 다섯 탑이 왼쪽으로 동시에 레이저 신호를 발사합니다.
# 그러면, 탑은 다음과 같이 신호를 주고 받습니다.
#
# 높이가 4인 다섯 번째 탑에서 발사한 신호는 높이가 7인 네 번째 탑에서 수신하고,
# 높이가 7인 네 번째 탑의 신호는 높이가 9인 두 번째 탑이,
# 높이가 5인 세 번째 탑의 신호도 높이가 9인 두 번째 탑이 수신합니다.
#
# 높이가 9인 두 번째 탑과 높이가 6인 첫 번째 탑이 보낸 레이저 신호는
# 어떤 탑에서도 수신할 수 없습니다.
#
# 이 때, 맨 왼쪽부터 순서대로 탑의 높이를 담은 배열 heights가 매개변수로 주어질 때
# 각 탑이 쏜 신호를 어느 탑에서 받았는지 기록한 배열을 반환하시오.
# 만약 신호를 수신하는 탑이 없으면 0으로 표시합니다.

# [6, 9, 5, 7, 4] # 라고 입력된다면,
#
# # 아래 그림처럼 탑이 있다고 보시면 됩니다!
# <- <- <- <- <- 레이저의 방향
#    I
#    I
#    I     I
# I  I     I
# I  I  I  I
# I  I  I  I  I
# I  I  I  I  I
# I  I  I  I  I
# I  I  I  I  I
#
# [0, 0, 2, 2, 4] # 다음과 같이 반환하시면 됩니다!

top_heights = [6, 9, 5, 7, 4]
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

#내풀이:
#맨 끝에 값을 뺀 후에 나머지 배열 맨 뒤에서부터 크기 비교
#더 큰값의 인덱스를 스택에 삽입
#완성된 스택을 순서대로 pop 하면서 다시 배열에 삽입
def get_receiver_top_orders_1(heights):
    answer = []
    stack = Stack()
    while len(heights) > 1:
        popped = heights.pop()
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] >= popped: #수신 받는 탑이 몇번째 탑인지
                stack.push(i + 1)
                break
        else:
            stack.push(0) # 왼쪽에 더 높은 탑이 없는 것이기 때문에 0
    stack.push(0) # 마지막 탑은 왼쪽에 아무 탑도 없기 때문에 0
    while not stack.is_empty():
        answer.append(stack.pop().data)
    return answer

#강의 풀이
def get_receiver_top_orders_2(heights):
    answer = [0] * len(heights)

    while heights: # heights 가 비어있지 않을때 True 반환
        height = heights.pop()
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] >= height:
                answer[len(heights)] = i + 1
                break

    return answer
print(get_receiver_top_orders_1(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!

print("정답 = [0, 0, 2, 2, 4] / 현재 풀이 값 = ", get_receiver_top_orders_1([6, 9, 5, 7, 4]))
print("정답 = [0, 0, 2, 3, 3, 3, 6] / 현재 풀이 값 = ", get_receiver_top_orders_1([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [0, 0, 2, 0, 0, 5, 6] / 현재 풀이 값 = ", get_receiver_top_orders_1([1, 5, 3, 6, 7, 6, 5]))
print("---개선안---")
print("정답 = [0, 0, 2, 2, 4] / 현재 풀이 값 = ", get_receiver_top_orders_2([6, 9, 5, 7, 4]))
print("정답 = [0, 0, 2, 3, 3, 3, 6] / 현재 풀이 값 = ", get_receiver_top_orders_2([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [0, 0, 2, 0, 0, 5, 6] / 현재 풀이 값 = ", get_receiver_top_orders_2([1, 5, 3, 6, 7, 6, 5]))