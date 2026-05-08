
def solution(targets):
    answer = 0

    sorted_targets = sorted(targets, key=lambda t: t[1])

    print(sorted_targets)

    idx = 0
    while idx < len(sorted_targets):
        end_point = sorted_targets[idx][1]
        for i in range(idx + 1, len(sorted_targets)):
            start_point = sorted_targets[i][0]
            if end_point <= start_point:
                print(i, "까지 격추가능")
                idx = i
                answer += 1
                break
        else:
            answer += 1
            idx = len(sorted_targets)

    print(answer)

    return answer

solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]])