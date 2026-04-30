# 각 n번 운송로봇의 첫 위치는 routes[n - 1][0] -> 두번째 경로 포인트 routes[n - 1][1].... -> m 번째 경로 포인트 routes[n][m - 1]
# 1초 마다 한 칸씩 이동, 최단경로로 이동
# 다음 포인트로 이동할 때 먼저 row 부터 움직임
# => 다음 포인트로 움직여야 하는 경로가 row : -2 col: +4라면 1초마다 routes[n - 1][0] = routes[n - 1][0] - 1 => 2번반복
# , routes[n - 1][1] = routes[n - 1][1] + 1 4번반복 순대로 라는 거임.
# 도착하면 바로 사라져버림
# 일단 운송로복 하나의 최종포인트까지의 순차적인 경로를 배열로 반환하는 함수 생성
def create_way_by_s(points, one_routes):
    all_way_s = [(points[one_routes[0] - 1][0], points[one_routes[0] - 1][1])]
    for i in range(len(one_routes) - 1):
        r = points[one_routes[i + 1] - 1][0] - points[one_routes[i] - 1][0]
        print("row 차이: ", r)
        c = points[one_routes[i + 1] - 1][1] - points[one_routes[i] - 1][1]
        print("col차이: ", c)
        init_row_loc = points[one_routes[i] - 1][0]
        init_col_loc = points[one_routes[i] - 1][1]
        if r > 0:
            for j in range(r):
                init_row_loc += 1
                all_way_s.append((init_row_loc, init_col_loc))
        elif r < 0:
            for j in range(-r):
                init_row_loc -= 1
                all_way_s.append((init_row_loc, init_col_loc))
        if c > 0:
            for j in range(c):
                init_col_loc += 1
                all_way_s.append((init_row_loc, init_col_loc))
        elif c < 0:
            for j in range(-c):
                init_col_loc -= 1
                all_way_s.append((init_row_loc, init_col_loc))

    print(all_way_s)
    return all_way_s

def find_loc(robot_all_way, s):
    if len(robot_all_way) <= s:
        return None
    else:
        return robot_all_way[s]

def solution(points, routes):
    answer = 0
    finish = [False] * len(routes)
    all_robot_way = []
    for route in routes:
        all_robot_way.append(create_way_by_s(points, route))
    print(all_robot_way)
    s = 0

    crash_cnt = 0
    while False in finish:
        check_crash = set()
        crash_occur_loc = set()
        for idx, way in enumerate(all_robot_way) :
            loc = find_loc(way, s)
            if loc is None:
                finish[idx] = True
            else:
                if loc in check_crash:
                    print(s, "초일 때", loc,"에서 충돌 발생!")
                    crash_occur_loc.add(loc)
                else:
                    check_crash.add(loc)
        crash_cnt += len(crash_occur_loc)
        s += 1

    return crash_cnt

print(solution([[3, 2], [6, 4], [4, 7], [1, 4]],[[4, 2], [1, 3], [2, 4]]))
print(solution([[3, 2], [6, 4], [4, 7], [1, 4]],[[4, 2], [1, 3], [4, 2], [4, 3]]))
print(solution([[2, 2], [2, 3], [2, 7], [6, 6], [5, 2]],[[2, 3, 4, 5], [1, 3, 4, 5]]))