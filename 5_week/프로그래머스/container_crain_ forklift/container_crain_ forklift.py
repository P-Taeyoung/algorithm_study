from collections import deque

def solution(storage, requests):
    row = len(storage)
    col = len(storage[0])
    storage_arr = [["."] * col for _ in range(row)]
    total_containers = row * col
    for i in range(row):
        for j in range(col):
            storage_arr[i][j] = storage[i][j]

    cnt = 0

    for selected_container in requests:
        cnt += can_carry(storage_arr, selected_container)

    return total_containers - cnt


def can_carry(storage_arr, alp):
    find_container = alp[0]
    to_remove = []

    row_len = len(storage_arr)
    col_len = len(storage_arr[0])

    for r in range(row_len):
        for c in range(col_len):
            if storage_arr[r][c] == find_container:
                # 1. "AA"처럼 두 글자면 무조건 삭제 대상
                if len(alp) > 1:
                    to_remove.append((r, c))
                # 2. 한 글자면 바깥과 닿아있는지 확인
                else:
                    if can_carry_by_fork(storage_arr, r, c):
                        to_remove.append((r, c))

    # 한꺼번에 지우기
    for r, c in to_remove:
        storage_arr[r][c] = "."

    return len(to_remove)

def can_carry_by_fork(storage_arr, con_r, con_c):
    queue = deque([(con_r, con_c)])
    visited = [[False] * len(storage_arr[0]) for _ in range(len(storage_arr))]

    row_len = len(storage_arr)
    col_len = len(storage_arr[0])
    visited[con_r][con_c] = True  # 시작점 방문 처리

    while queue:
        r, c = queue.popleft()

        # 창고의 경계(패딩된 영역 포함)에 도달하면 외부와 연결된 것
        if r == 0 or r == row_len - 1 or c == 0 or c == col_len - 1:
            return True

        # 상하좌우 4방향 탐색
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc

            # 1. 범위 내에 있고
            if 0 <= nr < row_len and 0 <= nc < col_len:
                # 2. 방문한 적 없으며 3. 통로(".")인 경우에만 이동
                if not visited[nr][nc] and storage_arr[nr][nc] == ".":
                    visited[nr][nc] = True  # 큐에 넣을 때 즉시 방문 처리
                    queue.append((nr, nc))

    return False

print(solution(["AZWQY", "CAABX", "BBDDA", "ACACA"], ["A", "BB", "A"]))
print(solution(["HAH", "HBH", "HHH", "HAH", "HBH"], ["C", "B", "B", "B", "B", "H"]))