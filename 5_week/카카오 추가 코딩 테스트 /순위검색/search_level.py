# 조건에 해당하는 사람이 몇명인지 반환해야 함.
# 단순 반복문으로 풀면 시간이 너무 오래걸릴 수 있음
# 점수를 제외하고 나올 수 있는 조건 조합 수 => 3 * 2 * 2 * 2 = 24
# 나머지는 점수로 갈림
# 각 조건 조합 수 별로 나눈 뒤 조건에 해당하는 점수들을 나열하면 빠르게 탐색 가능하지 않을까?
# ex) {(java, backend, junior, pizza) : [100,150,180....]}
# 항상 정렬된 상태로 유지해야 함.
# -, java 등 조건 하나만 있을 때 해당 조건이 포함된 모든 키가 반환될 수 있도록 해야함.
# {"java" : "javabackendjuniorpizza", "javabackendjuniorpizza"}
import bisect
from bisect import bisect_left


def make_info_key_form(info):
    info_arr = info.split(" ")
    return (info_arr[0] , info_arr[1] , info_arr[2] , info_arr[3]), int(info_arr[4])

def make_query_key_form(query):
    query_remove_and = query.replace("and", " ")
    query_arr = query_remove_and.split()
    return (query_arr[0] , query_arr[1] , query_arr[2], query_arr[3]), int(query_arr[4])

def solution(info, query):
    answer = []
    conditions = [["cpp", "java", "python", "-"], ["backend", "frontend", "-"], ["junior", "senior", "-"], ["chicken", "pizza", "-"]]
    num_of_conditions = {}
    for i in range(len(conditions[0])):
        for j in range(len(conditions[1])):
            for k in range(len(conditions[2])):
                for l in range(len(conditions[3])):
                    num_of_conditions[(conditions[0][i], conditions[1][j] , conditions[2][k] , conditions[3][l])] = []


    for one_info in info:
        info_keys, info_score = make_info_key_form(one_info)
        for i in [info_keys[0], "-"]:
            for j in [info_keys[1], "-"]:
                for k in [info_keys[2], "-"]:
                    for l in [info_keys[3], "-"]:
                        num_of_conditions[(i, j, k, l)].append(info_score)

    # 모든 조건들에 대한 점수 리스트 정렬
    for scores in num_of_conditions.values():
        scores.sort()

    for one_query in query:
        query_keys, query_score = make_query_key_form(one_query)
        cnt = 0
        scores = num_of_conditions[query_keys]
        idx = bisect_left(scores, query_score)
        cnt += (len(scores) -idx)
        answer.append(cnt)

    print(num_of_conditions)

    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))