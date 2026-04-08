from collections import deque

c = 11
b = 2

# 11 -> 11 + 1 -> (11 + 1) + 1 + 1 -> (11 + 1 + 1) + 2 + 1 -> 11 + 3 + 1 => arr[idx + 1] = arr[idx] + k(그전이동거리) + 1
# k = arr[idx] - arr[idx - 1]
# 이동거리 => n + 1
# arr[idx + 1] = arr[idx] + n
# c + 1 -> c + 1 + 2 -> c + 1 + 2 + 3 -> c + 1 + 2 + 3 + 4

# 내풀이
# 큐를 이용하여 BFS 구현
# 브라운은 다음 경우의 수가 총 3가지 즉 3 * 3 * 3 => 3 ^ n 의 형식이 될 것
# 몇번째 탐색인지 알기 위해 키 값 형태로 큐에 삽입 ex) 1번째 : 3
# 현재 간격은 9일 때, 11 + 1 로 갈때 2 + 1, 2 - 1, 2 * 2 경우의 수가 있음 이 경우의수를 차례대로 큐에 다시 삽입
def catch_me(cony_loc, brown_loc):
    # 구현해보세요!
    arr = []
    i = 0 #  이동 횟수
    c_d = 0 # 코니가 매초마다 이동하는 거리
    que = deque()
    arr.append(que)
    arr[i].append(brown_loc)
    while cony_loc <= 200000 and cony_loc >= 0:
        queue = deque()
        visited = set()
        arr.append(queue)
        # print("탐색 시간: ", i)
        while arr[i]:
            brown_loc_num = arr[i].popleft()
            # print("탐색값: ", brown_loc_num)
            if brown_loc_num == cony_loc:
                return i

            new_position = brown_loc_num - 1
            if new_position > 0 and new_position not in visited:
                visited.add(new_position)
                arr[i + 1].append(new_position)

            new_position = brown_loc_num + 1
            if new_position < 200001 and new_position not in visited:
                visited.add(new_position)
                arr[i + 1].append(new_position)

            new_position = brown_loc_num * 2
            if new_position < 200001 and new_position not in visited:
                visited.add(new_position)
                arr[i + 1].append(new_position)
                

        i += 1
        c_d += 1
        cony_loc += c_d

    return "코니가 도망갔습니다."

def catch_me_1(cony_loc, brown_loc):
    time = 0
    queue = deque()
    queue.append((brown_loc, 0))  # 위치와 시간을 담아줄게요!.
    visited = [{} for _ in range(200001)]

    while cony_loc < 200000:
        cony_loc += time
        if time in visited[cony_loc]:
            return time
        print("탐색시간: ", time)
        for i in range(0, len(queue)):  # Q. Queue 인데 while 을 안 쓰는 이유를 고민해보세요! => 해당 초에 방문한 노드만 탐색하기 위하여
            current_position, current_time = queue.popleft()
            print("탐색값: ", current_position)

            new_position = current_position - 1
            new_time = current_time + 1
            if new_position >= 0 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position + 1
            if new_position < 200001 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position * 2
            if new_position < 200001 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

        time += 1

# print(catch_me(c, b))  # 5가 나와야 합니다!
print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))

# print(catch_me_1(c, b))  # 5가 나와야 합니다!
# print("정답 = 3 / 현재 풀이 값 = ", catch_me_1(10,3))

