# 가장 많은 석유를 뽑아낼 수 있는 위치를 구하라
# 1. 석유관이 꼽혔을 때 석유가 있는 모든 연속된 칸을 구해 총 몇칸의 석유가 있는 지 구해내야 함.
# -> 석유칸에 관이 도달했을 때 해당 칸부터 동서남북으로 탐색하면서 석유가 있는 곳이면 카운트를 셈.
# -> 다 세고 나면 딕셔너리를 생성하여 해당 칸의 좌표에 석유가 얼마나 들었었는지 삽입
# ex) {[(1,2) : (0번째, 8)],[(1,3) : (0번째, 8)]}
# 2. 이미 한번 영역을 구한 석유칸은 다시 탐색하지 않도록 해야 함.
# -> 이미 탐색했던 칸의 좌표는 새로 생성한 딕셔너리에 있을 것이고 이와 함께 해당 칸을 통해 뽑아쓸 수 있는 석유의 양이 값으로 저장되어있을 것
# -> 이를 통해 이미 탐색한 석유칸은 계산을 하지 않고 바로 넘어갈 수 있음.

# 해당칸을 통해 뽑을 수 있는 석유의 양 구하는 함수
from collections import deque


def get_all_oil(land, r, c, dic, n):
    # 동 남 서 북
    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]

    dq = deque([[r, c]])
    visited = [[False] * len(land[0]) for _ in range(len(land))]
    # 석유관이 처음 맞닿은 곳 초기화
    visited[r][c] = True
    sum_oil = 1
    while dq:
        cur_r, cur_c = dq.popleft()
        for r, c in zip(dr, dc):
            new_r, new_c = cur_r + r, cur_c + c
            if len(land) > new_r >= 0 and len(land[0]) > new_c >= 0 and land[new_r][new_c] == 1 and not visited[new_r][new_c]:
                print("석유 + 1 좌표값: ", new_r, new_c)
                dq.append([new_r, new_c])
                visited[new_r][new_c] = True
                sum_oil += 1
                dic[(new_r, new_c)] = n

    return sum_oil


def solution(land):
    answer = 0
    area_sum_oil = {}
    have_oil = {}
    n = 0
    max_sum_oil = 0
    for c in range(len(land[0])):
        visited_area = set()
        cur_sum_oil = 0
        for r in range(len(land)):
            print("경로 탐색", r, c)
            if land[r][c] == 1:
                # 해당 구역에 석유가 있지만 아직 얼마나 있는지 모를때
                if (r, c) not in have_oil.keys():
                    sum_oil = get_all_oil(land, r, c, have_oil, n)
                    area_sum_oil[n] = sum_oil
                    print(n, "번 구역에는 총 ", sum_oil, "이 저장되어 있음")
                    visited_area.add(n)
                    cur_sum_oil += area_sum_oil[n]
                    # 다음 발견구역은 새로운 구역이므로
                    n += 1
                else:
                # 이미 해당 구역에 저장되어 있는 석유량을 알지만 새로운 경로 탐색중일 때
                    if have_oil[(r, c)] not in visited_area:
                        print("새로운 경로 탐색 중", have_oil[(r, c)], "번 구역 통과")
                        cur_sum_oil += area_sum_oil[have_oil[(r, c)]]
                        visited_area.add(have_oil[(r, c)])
        max_sum_oil = max(max_sum_oil, cur_sum_oil)

    return max_sum_oil


print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]))
print(solution([[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]))
