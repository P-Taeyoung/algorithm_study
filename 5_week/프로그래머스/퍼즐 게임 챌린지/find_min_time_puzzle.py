
# level = 3
# diffs[0] - 3 = - 2 < 0 -> 2
# diffs[1] - 3 = 2 > 0 -> (2 + 4) * 2 + 4 -> 16
# diffs[2] - 3 = 0 = 0 -> 7
# = 25
# 제한 시간내 풀기 위해서는 숙련도 3이 제일 최솟값임.
# 최솟값이라면 이분탐색??
# diffs를 정렬후 최솟값과 최댓값의 중간값을 구한뒤 숙련도로 정함
# 해당 숙련도로 시간을 구할 때
# 만약 시간을 구하다가 limit을 넘어버리면 즉 시간 내 해당 숙련도로 모든 퍼즐을 풀지 못하면 중간값과 최댓값 사이의 중간값으로 다시 숙련도를 정해서 시도
# 시간 내 풀 수 있으면 최솟값과 중간값 사이의 중간값으로 다시 숙련도를 정해서 시도
# [2, 4, 7] 일 때 기본 풀이시간 2 + 4 + 7 에 2번 퍼즐을 한번 틀릴때마다 6씩 3번퍼즐을 틀릴 때마다 11씩 늘어남
# [6, 3, 8, 2]일 때 기본 풀이시간 6 + 3 + 4 + 2 에 2번 퍼즐은 9, 3번 퍼즐은 11, 4번 퍼즐은 10씩 늘어남

def solution(diffs, times, limit):
    answer = 0
    sorted_diffs = sorted(diffs)
    # 각각 퍼즐 틀렸을 때 추가되는 시간 구하기
    plus_time = []
    for i in range(1, len(times)):
        plus_time.append(times[i - 1] + times[i])

    # 기본 풀이시간 구하기
    basic_time = 0
    for time in times:
        basic_time += time



    # 이분 탐색으로 최소시간 구하기
    min_time = 2
    max_time = sorted_diffs[-1]

    while min_time < max_time:
        total_time = basic_time
        mid_time = (min_time + max_time) // 2
        for i in range(1, len(diffs)):
            diff_num = mid_time - diffs[i]
            if diff_num < 0:
                total_time += (plus_time[i - 1] * abs(diff_num))
                if total_time > limit:
                    min_time = mid_time + 1
                    break
        if total_time <= limit:
            max_time = mid_time


    return max_time

print(solution([1, 5, 3], [2, 4, 7], 30))
print(solution([1, 4, 4, 2], [6, 3, 8, 2], 59))
print(solution([1, 328, 467, 209, 54], [2, 7, 1, 4, 3], 1723))
print(solution([1, 99999, 100000, 99995], [9999, 9001, 9999, 9001]	, 3456789012))
