def solution(players, m, k):
    living_server = [m] * 24
    answer_cnt = 0
    for i in range(24):
        if players[i] >= living_server[i]:
            cur_server = living_server[i]
            while players[i] >= cur_server:
                cur_server += m
                answer_cnt += 1
            for j in range(i + 1, min(i + k, 24)):
                will_server = cur_server - living_server[i]
                living_server[j] = living_server[j] + will_server
        print("현재 시간: ", i, "서버 상황: ",living_server)

    return answer_cnt

print(solution(	[0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5], 3, 5))