# Q.
# 문제 설명
# 로봇 청소기가 주어졌을 때, 청소하는 영역의 개수를 구하는 프로그램을 작성하시오.
# 로봇 청소기가 있는 장소는 N×M 크기의 직사각형으로 나타낼 수 있으며, 1×1크기의 정사각형 칸으로 나누어져 있다. 각각의 칸은 벽 또는 빈 칸이다.
# 청소기는 바라보는 방향이 있으며, 이 방향은 동, 서, 남, 북중 하나이다. 지도의 각 칸은 (r, c)로 나타낼 수 있고,
# r은 북쪽으로부터 떨어진 칸의 개수, c는 서쪽으로 부터 떨어진 칸의 개수이다.
# 로봇 청소기는 다음과 같이 작동한다.
# 1. 현재 위치를 청소한다.
# 2. 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다.
#     a. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
#     b. 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
#     c. 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
#     d. 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
# 로봇 청소기는 이미 청소되어있는 칸을 또 청소하지 않으며, 벽을 통과할 수 없다.
#
# 입력 조건
# 로봇 청소기가 있는 칸의 좌표 (r, c)와 바라보는 방향 d가 주어진다. 이 때 d가 0인 경우에는 북쪽을,
# 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽을 바라보고 있는 것이다.
#
# 또한 청소하고자 하는 방의 지도를 2차원 배열로 주어진다.
# 빈 칸은 0, 벽은 1로 주어진다. 지도의 첫 행, 마지막 행, 첫 열, 마지막 열에 있는 모든 칸은 벽이다.
#
# 로봇 청소기가 있는 칸의 상태는 항상 빈 칸이라고 했을 때,
# 로봇 청소기가 청소하는 칸의 개수를 반환하시오.
from collections import deque

current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# 내풀이
# DFS 방식으로 풀어야 함.
# 청소기가 이동하면 이동 전 자리는 청소했다는 표시를 남겨야 함.(이 때 1과는 구분되어야 함. 후진 규칙때문에 벽과 구분되어야 함.)
# 청소기 동작 방식
# 1. 왼쪽방향으로 돌면서 (처름 바라보는 방향쪽부터 탐색x)
# 2. 청소를 한 적이 있는지 아니면 벽인지 확인 (실제 회전)
# 3. 청소를 한 적이 있거나 벽이면 1번으로 돌아가 다시 반복
# 4. 청소를 한적이 없는 빈 공간인 경우 해당 좌표로 이동 (청소기가 바라보는 방향유지) (이동할 때 청소된 칸 카운트)
# 5. 만약 사방이 이미 청소되었거나 벽으로 막혀있다면 해당 방향에서 후진
# 6. 이 때 뒤가 벽으로 막혀있어 후진할 수 없다면 작동 중지
# 스택으로 풀이

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):

    #왼쪽 방향으로 회전
    # 주어진 위치가 7,4, 북 일때
    # 확인해야 하는 순서
    # -> 7, 3 서(3) -> [a][b - 1]
    # -> 8, 4 남(2) -> [a + 1][b]
    # -> 7, 5 동(1) -> [a][b + 1]
    # -> 6, 4 북(0) -> [a - 1][0]
    cnt = 1
    stack = []
    stack.append([r, c, d])
    while True:
        cur_space = stack.pop()
        # 청소한 위치 '2'로 체크
        room_map[cur_space[0]][cur_space[1]] = 2
        for r in range(3, -1, -1):
            direction = (cur_space[2] + r) % 4
            if direction == 0:
                if room_map[cur_space[0] - 1][cur_space[1]] == 0:
                    stack.append([cur_space[0] - 1,cur_space[1],0])
                    cnt += 1
                    break
            elif direction == 1:
                if room_map[cur_space[0]][cur_space[1] + 1] == 0:
                    stack.append([cur_space[0],cur_space[1] + 1,1])
                    cnt += 1
                    break
            elif direction == 2:
                if room_map[cur_space[0] + 1][cur_space[1]] == 0:
                    stack.append([cur_space[0] + 1,cur_space[1],2])
                    cnt += 1
                    break
            elif direction == 3:
                if room_map[cur_space[0]][cur_space[1] - 1] == 0:
                    stack.append([cur_space[0],cur_space[1] - 1,3])
                    cnt += 1
                    break
        else:
            direction = (cur_space[2] + 2) % 4
            if direction == 0:
                if room_map[cur_space[0] - 1][cur_space[1]] == 1:
                    break
                else:
                    stack.append([cur_space[0] - 1,cur_space[1], cur_space[2]])
            elif direction == 1:
                if room_map[cur_space[0]][cur_space[1] + 1] == 1:
                    break
                else:
                    stack.append([cur_space[0],cur_space[1] + 1, cur_space[2]])
            elif direction == 2:
                if room_map[cur_space[0] + 1][cur_space[1]] == 1:
                    break
                else:
                    stack.append([cur_space[0] + 1,cur_space[1], cur_space[2]])
            elif direction == 3:
                if room_map[cur_space[0]][cur_space[1] - 1] == 1:
                    break
                else:
                    stack.append([cur_space[0],cur_space[1] - 1, cur_space[2]])
    return cnt




# 57 가 출력되어야 합니다!
print("정답 = 57 / 현재 풀이 값 = ",get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))
current_room_map2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
print("정답 = 29 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(6,3,1,current_room_map2))
current_room_map3 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
print("정답 = 33 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(7,4,1,current_room_map3))
current_room_map4 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
print("정답 = 25 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(6,2,0,current_room_map4))