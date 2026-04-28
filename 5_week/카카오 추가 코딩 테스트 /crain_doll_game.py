# 내풀이
# stack을 이용하여 풀 수 있을 듯
# 가로로 기준이 되어 있는 배열을 문제풀기가 쉽게 세로로 기준으로 각 [[스택1], [스택2]..] 이러한 식으로 옮김.
# 바구니는 스택 구조로 생성 후 인형을 삽입
# 인형을 바구니로 옮기기 전 맨 끝에 삽입된 인형을 꺼내 비교
# 같다면 카운트 횟수 이때 사라진 인형의 갯수이기 때문에 2개 추가

def solution(board, moves):
    answer = 0
    n = len(board)
    m = len(board[0])
    doll_case = [[] for _ in range(m)]
    picked_case = []
    for i in range(len(board) - 1, -1, -1):
        for j in range(len(board[0])):
            if board[i][j] != 0:
                doll_case[j].append(board[i][j])

    for i in moves:
        if not doll_case[i - 1]:
            continue

        picked_doll = doll_case[i - 1].pop()
        if picked_case:
            if picked_case[-1] == picked_doll:
                answer += 2
                picked_case.pop()
            else:
                picked_case.append(picked_doll)
        else:
            picked_case.append(picked_doll)

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))