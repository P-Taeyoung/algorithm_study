
def find_time(end_time, t):
    h_m_s_ms = end_time.split(":")

    h = int(h_m_s_ms[0])
    m = int(h_m_s_ms[1])

    s_ms = h_m_s_ms[2].split(".")
    s = int(s_ms[0])
    ms = int(s_ms[1])

    int_end_time = (h * 3600000) + (m * 60000) + (s * 1000) + ms

    play_time = t[:-1].split(".")

    if len(play_time) == 1:
        return int_end_time - (int(play_time[0]) * 1000) + 1, int_end_time
    else:
        return int_end_time - ((int(play_time[0]) * 1000) + int(play_time[1])) + 1, int_end_time


def solution(lines):
    answer = 0
    all_time = []
    search_time = []
    for line in lines:
        task_info = line.split(" ")
        end_time = task_info[1]
        t = task_info[2]
        all_time.append(find_time(end_time, t))
        search_time.extend(find_time(end_time, t)) # 일차원 배열로 삽입하여 탐색시간을 정함.

    print(all_time)

    max_cnt = 0
    for t_idx, t in enumerate(search_time):
        cnt = 0
        for i in range(t_idx // 2, len(all_time)):
            #시작시간이 탐색 시간의 종료시간보다 크거나 종료시간이 탐색시간의 시작시간보다 이전이면 해당 요청은 탐색시간내 처리되지 않은것임
            if not(all_time[i][1] < t or all_time[i][0] >= t + 1000):
                print("탐색구간 :", t, "~", t + 1000, "포함되는 처리 요청 시간", all_time[i])
                cnt += 1
        max_cnt = max(max_cnt, cnt)

    print(max_cnt)
    return answer


print(solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]))

