# 입력된 정수와 시스템응답을 보고 가능한 비밀코드의 수를 구하시오.
# n까지의 수 중에서 5개로 이루어진 모든 경우의 수를 뽑아냄
# q와 비교하면서 시스템 응답수와 맞지 않는다면 탐색 중단. 시스템 응답에 다 통과한다면 해당 수는 비밀코드가 될 수 있음.
# 시간 복잡더가 꽤 있음

import itertools

def solution_1(n, q, ans):
    answer = 0
    nums = [i for i in range(1, n + 1)]
    can_password = list(itertools.combinations(nums, 5))

    print(can_password)

    for password in can_password:
        for i, try_pass in enumerate(q):
            include_nums = 0
            sys_answer = ans[i]
            for idx, num in enumerate(try_pass):
                if num in password:
                    include_nums += 1
            if include_nums != sys_answer:
                break
        else:
            answer += 1

    return answer


def solution_2(n, q, ans):
    answer = 0
    q_sets = [set(query) for query in q]
    nums = range(1, n + 1)

    for password in itertools.combinations(nums, 5):
        password_set = set(password)

        is_match = True
        for i in range(len(q)):
            if len(password_set & q_sets[i]) != ans[i]:
                is_match = False
                break
        if is_match:
            answer += 1

    return answer


# print(solution_1(30, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]], [2, 3, 4, 3, 3]))
print(solution_2(30, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7], [1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]], [2, 3, 4, 3, 3, 2, 3, 4, 3, 3]))