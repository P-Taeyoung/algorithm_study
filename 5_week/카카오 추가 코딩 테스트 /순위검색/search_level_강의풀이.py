# 결과 코드

from itertools import combinations


def make_all_cases(temp):
    cases = []
    for i in range(5):
        for combination in combinations([0, 1, 2, 3], i):
            case = ''
            for idx in range(4):
                if idx not in combination:
                    case += temp[idx]
                else:
                    case += '-'
            cases.append(case)
    return cases


def get_lower_bound(target, array):
    current_min = 0
    current_max = len(array)

    while current_min < current_max:
        current_guess = (current_min + current_max) // 2
        if array[current_guess] >= target:
            current_max = current_guess
        else:
            current_min = current_guess + 1

    return current_max


def solution(info, query):
    answer = []
    all_cases_from_users = {}
    for user_info in info:
        user_info_array = user_info.split()
        all_cases_from_user = make_all_cases(user_info_array)
        for case in all_cases_from_user:
            if case not in all_cases_from_users.keys():
                all_cases_from_users[case] = [int(user_info_array[4])]
            else:
                all_cases_from_users[case].append(int(user_info_array[4]))

    for key in all_cases_from_users.keys():
        all_cases_from_users[key].sort()

    for query_info in query:
        query_info_array = query_info.split()
        case = query_info_array[0] + query_info_array[2] + query_info_array[4] + query_info_array[6]
        if case in all_cases_from_users.keys():
            target_users = all_cases_from_users[case]
            answer.append(
                len(target_users) - get_lower_bound(int(query_info_array[7]), target_users)
            )
        else:
            answer.append(0)

    return answer