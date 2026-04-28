
from collections import deque

k = 4  # 말의 개수

chess_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
start_horse_location_and_directions = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
# 이 경우는 게임이 끝나지 않아 -1 을 반환해야 합니다!
# 동 서 북 남
# →, ←, ↑, ↓



# 내 풀이
# 체스맵 구조로 배열로 구성된 이중 배열을 생성
# [[deque1], [deque2]]
# [[deque3], [deque4]]
# => 이를 통해 말의 위치와 현재 상태(말 쌓임상태)를 쉽게 저장할 수 있도록 함.
# 배열에 저장할 때 말번호만 저장
# 현재 위치 정보와 방향정보는 start_horse_location_and_directions 배열 변수를 통해 계속 갱신해나가면서 저장
# 각 발판 기능을 하는 함수를 선언
# 움직이기 전에 먼저 확인
def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    answer = -1
    arr_map = [[[] for _ in range(len(game_map[0]))] for _ in range(len(game_map))]
    dr = [0, 0, -1, 1]
    dc = [1, -1, 0, 0]
    for horse_num in range(0, horse_count):
        arr_map[horse_location_and_directions[horse_num][0]][horse_location_and_directions[horse_num][1]].append(horse_num)

    for i in range(1, 1001):
        for k in range(0, horse_count):
            will_moved_row, will_moved_col = check_next(horse_location_and_directions, k, dr, dc)
            if 0 <= will_moved_row < len(game_map) and 0 <= will_moved_col < len(game_map[0]):
                if game_map[will_moved_row][will_moved_col] == 0:
                    moved(horse_location_and_directions, k, will_moved_row, will_moved_col, arr_map)
                elif game_map[will_moved_row][will_moved_col] == 1:
                    moved(horse_location_and_directions, k, will_moved_row, will_moved_col, arr_map)
                    red(horse_location_and_directions, k, arr_map)
                elif game_map[will_moved_row][will_moved_col] == 2:
                    blue(horse_location_and_directions, k, dr, dc, arr_map, game_map)
            else:
                blue(horse_location_and_directions, k, dr, dc, arr_map, game_map)
            if len(arr_map[horse_location_and_directions[k][0]][horse_location_and_directions[k][1]]) >= 4:
                answer = i
                return answer

    return answer

# 다음 움직였을 때 발판 색깔이 무엇인지 확인하기 위한 함수
def check_next(horse_arr, horse_num, dr, dc):
    row = dr[horse_arr[horse_num][2]]
    col = dc[horse_arr[horse_num][2]]
    will_moved_row = horse_arr[horse_num][0] + row
    will_moved_col = horse_arr[horse_num][1] + col
    return will_moved_row, will_moved_col

#업힌 말 포함 움직이는 함수
def moved(horse_arr, horse_num, moved_row, moved_col, arr_map):
    # 1. 현재 위치 파악
    r, c = horse_arr[horse_num][0], horse_arr[horse_num][1]

    # 2. 현재 칸에서 해당 말이 몇 번째 높이에 있는지 인덱스 찾기
    idx = arr_map[r][c].index(horse_num)

    # 3. 이동할 말들 슬라이싱 (해당 말부터 끝까지)
    moving_horses = arr_map[r][c][idx:]

    # 4. 이동할 말들의 좌표 정보 업데이트 및 목적지에 추가
    for h in moving_horses:
        horse_arr[h][0] = moved_row
        horse_arr[h][1] = moved_col

    # 목적지 칸 뒤에 통째로 붙이기
    arr_map[moved_row][moved_col].extend(moving_horses)

    # 5. 기존 칸에서 이동한 말들 한꺼번에 삭제
    del arr_map[r][c][idx:]


#파란 블록일 때 동작하는 함수
#방향을 정반대로 바꿔줌
#움직일 수 있는 상황이라면 말을 움직이도록 함
def blue(horse_arr, horse_num, dr, dc, arr_map, game_map):
    if horse_arr[horse_num][2] == 0:
        horse_arr[horse_num][2] = 1
    elif horse_arr[horse_num][2] == 1:
        horse_arr[horse_num][2] = 0
    elif horse_arr[horse_num][2] == 2:
        horse_arr[horse_num][2] = 3
    elif horse_arr[horse_num][2] == 3:
        horse_arr[horse_num][2] = 2
    will_moved_row, will_moved_col = check_next(horse_arr, horse_num, dr, dc)
    if 0 <= will_moved_row < len(arr_map) and 0 <= will_moved_col < len(arr_map[0]):
        if game_map[will_moved_row][will_moved_col] == 0:
            moved(horse_arr, horse_num, will_moved_row, will_moved_col, arr_map)
        elif game_map[will_moved_row][will_moved_col] == 1:
            moved(horse_arr, horse_num, will_moved_row, will_moved_col, arr_map)
            red(horse_arr, horse_num, arr_map)


#빨간 블록일 때 동작하는 함수
#슬라이싱을 통해 현재 말부터 업힌 말의 순서 바꿈
def red(horse_arr, horse_num, arr_map):
    row, col = horse_arr[horse_num][0], horse_arr[horse_num][1]
    idx = arr_map[row][col].index(horse_num)
    arr_map[row][col][idx:] = arr_map[row][col][idx:][::-1]




print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))  # 2가 반환 되어야합니다

start_horse_location_and_directions = [
    [0, 1, 0],
    [1, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
print("정답 = 9 / 현재 풀이 값 = ", get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))

start_horse_location_and_directions = [
    [0, 1, 0],
    [0, 1, 1],
    [0, 1, 0],
    [2, 1, 2]
]
print("정답 = 3 / 현재 풀이 값 = ", get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))


game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]
