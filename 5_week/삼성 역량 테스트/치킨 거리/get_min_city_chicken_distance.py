import itertools, sys

n = 5
m = 3

city_map = [
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 1],
    [0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2],
]
from itertools import combinations
# 내풀이
# 프로그래머스 완전범죄와 비슷한 문제인듯 함.
# M개 만큼 치킨집의 조합 뽑음.
# 각 집마다 조합에 해당하는 치킨 집 중 가장 작은 숫자 고름
# 가장 작은 숫자를 고를 때는 미리 거리 순으로 정렬시켜놓은 딕셔너리(치킨집 : 거리)를 통해 바로
def get_min_city_chicken_distance(n, m, city_map):
    chicken_stores = []
    citizens = []
    for i in range(n):
        for j in range(n):
            if city_map[i][j] == 2:
                chicken_stores.append((i, j))
            elif city_map[i][j] == 1:
                citizens.append((i, j))
    distances = []

    for city_p in citizens:
        city_p_dict = {}
        r1, c1 = city_p
        for chicken_store in chicken_stores:
            r2, c2 = chicken_store
            city_p_dict[chicken_store] = abs(r1 - r2) + abs(c1 - c2)
        distances.append(city_p_dict)

    combination_of_m = list(itertools.combinations(chicken_stores, m))

    min_cum_distance = sys.maxsize

    #조합을 반복하면 해당조합에서 각 집마다 치킨집과의 거리에서 가장작은수를 구하고 거리를 더함,
    for combi in combination_of_m:
        cur_min_distance = 0
        for distance in distances:
            min_dis = distance[min((k for k in combi if k in distance), key=distance.get)]
            cur_min_distance += min_dis
        if cur_min_distance < min_cum_distance:
            min_cum_distance = cur_min_distance


    return min_cum_distance


# 출력
print(get_min_city_chicken_distance(n, m, city_map))  # 5 가 반환되어야 합니다!


city_map = [
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0],
    [1, 2, 0, 0, 0]
]
print("정답 = 11 / 현재 풀이 값 = ", get_min_city_chicken_distance(5,1,city_map))


city_map = [
    [0, 2, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [2, 0, 0, 1, 1],
    [2, 2, 0, 1, 2]
]
print("정답 = 10 / 현재 풀이 값 = ", get_min_city_chicken_distance(5,2,city_map))

city_map = [
    [1, 2, 0, 2, 1],
    [1, 2, 0, 2, 1],
    [1, 2, 0, 2, 1],
    [1, 2, 0, 2, 1],
    [1, 2, 0, 2, 1]
]
print("정답 = 32 / 현재 풀이 값 = ", get_min_city_chicken_distance(5,1,city_map))