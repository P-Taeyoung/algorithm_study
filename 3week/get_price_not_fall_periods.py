# ❓ Q.
#
# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때,
# 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 함수를 완성하세요.
#
# prices = [1, 2, 3, 2, 3]
# answer = [4, 3, 1, 1, 0]

# 예를 들어서 0번째 인덱스인 1의 경우 오른쪽 방향으로 주식가격을 보면서
# 가격이 떨어졌는지 여부를 파악하게 됩니다.
#    -> -> -> ->
# [1, 2, 3, 2, 3] (전부 안떨어졌으니까 4초!)
#
# 1번째 인덱스인 2의 경우 오른쪽 방향으로 주식가격을 보면서
# 가격이 떨어졌는지 여부를 파악하게 됩니다.
#       -> -> ->
# [1, 2, 3, 2, 3] (전부 안떨어졌으니까 3초!)
#
# 2번째 인덱스인 3의 경우 오른쪽 방향으로 주식가격을 보면서
# 가격이 떨어졌는지 여부를 파악하게 됩니다.
#          ->
# [1, 2, 3, 2, 3] (1초 뒤에 떨어졌으니까 1초)
#
# 3번째 인덱스인 2의 경우 오른쪽 방향으로 주식가격을 보면서
# 가격이 떨어졌는지 여부를 파악하게 됩니다.
#             ->
# [1, 2, 3, 2, 3] (전부 안떨어졌으니까 1초)
#
# 4번째 인덱스인 3의 경우에는 마지막이라서 0초간 안 떨어집니다.
# [1, 2, 3, 2, 3]
from collections import deque

prices = [1, 2, 3, 2, 3]

# 내풀이
# 큐에는 인덱스를 추가
# 인덱스에 해당하는 배열값을 비교하여 가격이 떨어지지 않았으면 다시 해당 인덱스를 큐에 추가
# 큐에 추가될 때 마다 1초 증가
# 가격이 떨어진 경우에는 인덱스를 큐에 추가하지 않음. (초가 더 추가되지 않을 수 있도록)
def get_price_not_fall_periods_1(prices):
    # 이 부분을 채워주세요!
    answer_list = [0] * len(prices)
    queue = deque()

    for i in range(0, len(prices)):
        queue.append(i)
        while queue[0] != i:
            k = queue.popleft()
            answer_list[k] += 1

            if prices[k] <= prices[i]:
                queue.append(k)

    return answer_list

def get_price_not_fall_periods_2(prices):
    result = []
    prices = deque(prices)

    while prices:
        price_not_fall_period = 0
        current_price = prices.popleft()
        for next_price in prices:
            if current_price > next_price:
                price_not_fall_period += 1
                break
            price_not_fall_period += 1

        result.append(price_not_fall_period)

    return result

print(get_price_not_fall_periods_1(prices))

print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods_1(prices))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods_1([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods_1([1, 5, 3, 6, 7, 6, 5]))

print(get_price_not_fall_periods_2(prices))

print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods_2(prices))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods_2([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods_2([1, 5, 3, 6, 7, 6, 5]))
