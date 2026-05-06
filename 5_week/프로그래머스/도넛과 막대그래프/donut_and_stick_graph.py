

# 정점으로부터 나가는 간선이 2개이상일 경우 새로운 정점 or 8자 그래프
#

from collections import defaultdict

def solution(edges):
    linked_nodes = defaultdict(lambda: [0, 0])
    new_node = 0
    all_graph_cum = 0
    stick_graph_cum = 0
    eight_graph_cum = 0


    for edge in edges:
        from_node, to_node = edge[0], edge[1]
        linked_nodes[from_node][0] += 1
        linked_nodes[to_node][1] += 1

    for node in linked_nodes.keys():
        if linked_nodes[node][0] >= 2 and linked_nodes[node][1] == 0:
            new_node = node
            all_graph_cum = linked_nodes[node][0]
        elif linked_nodes[node][0] == 0 and linked_nodes[node][1] >= 0:
            stick_graph_cum += 1
        elif linked_nodes[node][0] == 2 and linked_nodes[node][1] >= 2:
            eight_graph_cum += 1

    donut_graph_cum = all_graph_cum - (stick_graph_cum + eight_graph_cum)

    answer = [new_node, donut_graph_cum, stick_graph_cum, eight_graph_cum]

    return answer

print(solution([[2, 3], [4, 3], [1, 1], [2, 1]]))
print(solution([[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]))