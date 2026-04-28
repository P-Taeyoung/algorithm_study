from collections import deque
import copy

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]

# 내풀이
# 구슬이 한번에 움직일 수 있는 경우가 총 4가지임(위, 아래, 오른쪽, 왼쪽) -> 경우의 수를 탐색하는 것이기 때문에 그래프 탐색 문제 (DFS or BFS)
# 빨간 구슬과 파란 구슬은 같은 방향으로 동시에 움직임
# 제약 조건
# 구슬 진행방향에 #, 다른 구슬이 있으면 움직이지 못함
# 다만 다른 구슬이 있는 경우, 해당 구슬이 다른 공간으로 이동하면서 공간이 생기면 이동 가능.
# -> 즉 다른 구슬이 있을 때, 그 구슬도 진행방향으로 움직이지 못하는 상황인 경우 움직이지 못함.
# 두 구슬이 더이상 움직이지 않을 때 멈춤
# 빨간 구슬을 10번 이하로 움직여 구멍에 빠트리면 성공 (true 반환)
# 10번 초과하여 움직여야 하거나, 파란 구슬이 그 전에 먼저 빠지면 실패 (False 반환)
# ---
# 빨간구슬과 파란구슬은 동시에 같은 방향으로 움직이므로 세트로 묶어서 하나의 경우의 수로 판단.
# 오른쪽으로 움직이는 경우: [빨간구슬의 위치 = [2,3],파란구슬의 위치 = [3,5]]
# 둘중 하나라도 움직일 수 있으면 계속 해당 방향으로 이동할 수 있도록 함. 둘다 해당 방향으로 못움직이면 경우의 수에서 배제
# 움직이기 전 해당 방향에 장애물이 있으면 해당 구슬은 위치 그대로 움직일 수 있는 구슬만 진행한 후 위치정보를 다시 큐에 삽입
#

def is_available_to_take_out_only_red_marble(game_map):
    # 구현해보세요!
    #현재 게임 맵 상의 구멍위치와 구슬 위치 초기화
    o = []
    r = []
    b = []
    find_init_loc = [False, False, False]
    for i in range(len(game_map)):
        if "O" in game_map[i]:
            idx = game_map[i].index("O")
            o.append(i)
            o.append(idx)
            find_init_loc[0] = True
        if "R" in game_map[i]:
            idx = game_map[i].index("R")
            r.append(i)
            r.append(idx)
            find_init_loc[1] = True
        if "B" in game_map[i]:
            idx = game_map[i].index("B")
            b.append(i)
            b.append(idx)
            find_init_loc[2] = True
        if False not in find_init_loc:
            break
    answer = -1
    queue = deque()
    queue.append((r,b,game_map))
    cnt = 1
    # 탐색한 위치는 다시 탐색하지 않게 하기 위해
    visited = []

    while cnt < 10:
        for i in range(len(queue)):
            red, blue, cur_map = queue.popleft()
            for j in range(4):
                new_red, new_blue, cur_map, is_red_goal, is_blue_goal = return_next_loc(cur_map, red, blue, j)
                if is_blue_goal:
                    continue
                elif is_red_goal:
                    return cnt
                else:
                    if [new_red, new_blue] not in visited:
                        visited.append([new_red, new_blue])
                        queue.append((new_red, new_blue, cur_map))
        cnt += 1

    return answer

def return_next_loc(game_map, red, blue, direction):
    # 오른쪽, 왼쪽, 아래, 위
    dr = [0, 0, -1, 1]
    dc = [1, -1, 0, 0]

    # 구슬이 해당 방향으로 움직였을 때 구멍에 빠지는 지 여부
    is_red_goal = False
    is_blue_goal = False

    # 현재 구슬의 위치
    cur_red_row = red[0]
    cur_red_col = red[1]
    cur_blue_row = blue[0]
    cur_blue_col = blue[1]

    # 경우의 수마다 맵 현황도 달라짐
    # next_map = game_map => 참조로 같은 값을 두변수가 가르키는 것임
    # game_map과 똑같이 생겼지만, 메모리 주소는 완전히 다른 새로운 배열 생성
    cur_map = copy.deepcopy(game_map)

    while True:
        # 다음 위치 미리 확인
        next_red_row = cur_red_row + dr[direction]
        next_red_col = cur_red_col + dc[direction]
        next_blue_row = cur_blue_row + dr[direction]
        next_blue_col = cur_blue_col + dc[direction]

        # 두 구슬 모두 움직이지 못하는 경우에 멈추고 그 때 구슬 위치를 반환
        # 두 구슬 모두 벽에 막혔을 때
        if cur_map[next_red_row][next_red_col] == "#" and cur_map[next_blue_row][next_blue_col] == "#":
            break
        # 다른 구슬에 막혀있고 다른 구슬은 벽에 막혔을 때
        elif cur_map[next_red_row][next_red_col] == "B" and cur_map[next_blue_row][next_blue_col] == "#":
            break
        elif cur_map[next_red_row][next_red_col] == "#" and cur_map[next_blue_row][next_blue_col] == "R":
            break
        # 다른 구슬은 구멍으로 빠져나갔고 다른 구슬은 벽에 막혔을 때
        elif cur_map[next_red_row][next_red_col] == "#" and is_blue_goal:
            break
        elif cur_map[next_blue_row][next_blue_col] == "#" and is_red_goal:
            break
        # 한 쪽 구슬이 먼저 구멍에 빠지는 경우
        elif cur_map[next_blue_row][next_blue_col] == "O" and not is_blue_goal:
            is_blue_goal = True
            cur_map[cur_blue_row][cur_blue_col] = "."
        elif cur_map[next_red_row][next_red_col] == "O" and not is_red_goal:
            is_red_goal = True
            cur_map[cur_red_row][cur_red_col] = "."
        else:
            #한 쪽만 움직일 수 있는 경우
            #다른 구슬이 벽때문에 못 움직이거나 이미 구멍에 들어간 경우
            if game_map[next_blue_row][next_blue_col] == "#" or is_blue_goal:
                cur_map[cur_red_row][cur_red_col] = "."
                cur_red_row += dr[direction]
                cur_red_col += dc[direction]
                cur_map[cur_red_row][cur_red_col] = "R"
            elif game_map[next_red_row][next_red_col] == "#" or is_red_goal:
                cur_map[cur_blue_row][cur_blue_col] = "."
                cur_blue_row += dr[direction]
                cur_blue_col += dc[direction]
                cur_map[cur_blue_row][cur_blue_col] = "B"
            #모두 움직일 수 있는 경우
            else:
                # 실제 구슬 위치 변경
                # 1. 구슬이 지나간 자리는 비어있음으로 변경
                cur_map[cur_red_row][cur_red_col] = "."
                cur_map[cur_blue_row][cur_blue_col] = "."
                # 2. 구슬 위치 옮김
                cur_red_row += dr[direction]
                cur_red_col += dc[direction]
                cur_blue_row += dr[direction]
                cur_blue_col += dc[direction]
                # 3. 옮긴 위치에 구슬 표기
                cur_map[cur_red_row][cur_red_col] = "R"
                cur_map[cur_blue_row][cur_blue_col] = "B"

    new_red = cur_red_row, cur_red_col
    new_blue = cur_blue_row, cur_blue_col

    return new_red, new_blue, cur_map, is_red_goal, is_blue_goal




print(is_available_to_take_out_only_red_marble(game_map))  # True 를 반환해야 합니다



game_map = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", "O", ".", ".", ".", ".", "R", "B", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]
print("정답 = False / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))


game_map = [
["#", "#", "#", "#", "#", "#", "#"],
["#", ".", ".", "R", "#", "B", "#"],
["#", ".", "#", "#", "#", "#", "#"],
["#", ".", ".", ".", ".", ".", "#"],
["#", "#", "#", "#", "#", ".", "#"],
["#", "O", ".", ".", ".", ".", "#"],
["#", "#", "#", "#", "#", "#", "#"]
]
print("정답 = True / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))

game_map = [
    ['#', '#', '#', '#', '#'],
    ['#', '.', '.', 'B', '#'],
    ['#', '.', '#', '.', '#'],
    ['#', 'R', 'O', '.', '#'],
    ['#', '#', '#', '#', '#']
]
print("정답 = 1 / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))


game_map = [
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', '.', '.', '.', 'R', 'B', '#'],
    ['#', '.', '#', '#', '#', '#', '#'],
    ['#', '.', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '#', '.', '#'],
    ['#', 'O', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '#', '#', '#']
]
print("정답 = 5 / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))


game_map = [
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', '.', '.', 'R', '#', 'B', '#'],
    ['#', '.', '#', '#', '#', '#', '#'],
    ['#', '.', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '#', '.', '#'],
    ['#', 'O', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '#', '#', '#']
]
print("정답 = 5 / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))

game_map = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], # 0
    ['#', 'R', '#', '.', '.', '.', '#', '#', 'B', '#'], # 1
    ['#', '.', '.', '.', '#', '.', '#', '#', '.', '#'], # 2
    ['#', '#', '#', '#', '#', '.', '#', '#', '.', '#'], # 3
    ['#', '.', '.', '.', '.', '.', '.', '#', '.', '#'], # 4
    ['#', '.', '#', '#', '#', '#', '#', '#', '.', '#'], # 5
    ['#', '.', '#', '.', '.', '.', '.', '#', '.', '#'], # 6
    ['#', '.', '#', '.', '#', '.', '#', '.', '.', '#'], # 7
    ['#', '.', '.', '.', '#', '.', 'O', '#', '.', '#'], # 8
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']  # 9
]
print("정답 = -1 / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))

game_map = [
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', 'R', '.', 'O', '.', 'B', '#'],
    ['#', '#', '#', '#', '#', '#', '#']
]
print("정답 = 1 / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))


game_map = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', 'R', '#', '.', '.', '.', '#', '#', 'B', '#'],
    ['#', '.', '.', '.', '#', '.', '#', '#', '.', '#'],
    ['#', '#', '#', '#', '#', '.', '#', '#', '.', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '#', '.', '#'],
    ['#', '.', '#', '#', '#', '#', '#', '#', '.', '#'],
    ['#', '.', '#', '.', '.', '.', '.', '#', '.', '#'],
    ['#', '.', '#', '.', '#', '#', '.', '.', '.', '#'],
    ['#', 'O', '.', '.', '#', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]
print("정답 = 7 / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))


game_map = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '.', 'O', '.', '.', '.', '.', 'R', 'B', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]
print("정답 = -1 / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))