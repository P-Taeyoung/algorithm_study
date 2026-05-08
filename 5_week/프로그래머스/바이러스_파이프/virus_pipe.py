# 내풀이
# 모든 조합을 구한뒤 (itertools를 사용) * 이 때 같은 파이프 타입은 연속해서 나올 수 없음.
# 해당 조합 순서대로 파이프를 열고 닫았을 때 감염되는 노드 수를 구하는 방법
# 감염되는 원리 -> 감염체와 인접한 노드 중 열린 파이프를 통해서만 감염됨.
# => 해당 파이프가 열렸을 때 감염되는 모든 노드 구하는 법
# a 파이프가 열렸을 때 감염되는 노드를 구하는 법 -> 첫번째 감염체와 인접한 노드 중 a파이프로 연결된 노드 감염되어 큐에 삽입
# -> 다시 큐를 돌아 2차 감염체들과 인접한 노드 중 a 파이프로 연결된 노드 감염 (더이상 감염되지 않을 때까지 즉, 큐에 더이상 노드가 들어오지 않을때까지 반복)
# [[[],[],[]],[[],[],[]] 3중 배열을 통해 각 노드에서 해당 파이프로 연결된
#
from collections import deque
from itertools import combinations, product


def infect(infections, nodes, pipes):

    for pipe in pipes:
        now_infections = deque(infections)
        while now_infections:
            infection = now_infections.popleft()
            for node in nodes[infection][pipe]:
                if node not in infections:
                    infections.add(node)
                    now_infections.append(node)

    return len(infections)


def find_comb(k):
    data = [0,1,2]

    all_comb = product(data, repeat = k)

    result = [
        p for p in all_comb
        if all(p[i] != p[i + 1] for i in range(k - 1))
    ]

    return result


def solution(n, infection, edges, k):
    #감염된 리스트 초기화


    #모든 파이프 순서 조합
    combs = find_comb(k)

    # 인접한 노드를 탐색하기 편한 상태로 [주인 노드[파이프[인접노드],[],[]],[[],[],[]] 만듦
    nodes = [[[] for _ in range(3)] for _ in range(n)] # 노드는 1부터 세도록
    for edge in edges:
        nodes[edge[0] - 1][edge[2] - 1].append(edge[1] - 1)
        nodes[edge[1] - 1][edge[2] - 1].append(edge[0] - 1)

    # 각 조합에서 나올 수 있는 최대 감염체 수 구하가
    max_infect_nodes = 0
    for comb in combs:
        infections = set()
        infections.add(infection - 1)
        max_infect_nodes = max(max_infect_nodes, infect(infections, nodes, comb))


    answer = max_infect_nodes
    return answer


print(solution(10, 1, [[1, 2, 1], [1, 3, 1], [1, 4, 3], [1, 5, 2], [5, 6, 1], [5, 7, 1], [2, 8, 3], [2, 9, 2], [9, 10, 1]], 2))
print(solution(7, 6, [[1, 2, 3], [1, 4, 3], [4, 5, 1], [5, 6, 1], [3, 6, 2], [3, 7, 2]], 3))
