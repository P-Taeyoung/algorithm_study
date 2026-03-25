# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}
visited = []

# 내 풀이
def dfs_recursion_1(adjacent_graph, cur_node, visited_array):
    # 구현해보세요!
    # 현재 노드 방문 기록
    visited.append(cur_node)
    # 현재 노드와 연결된 노드 확인
    node_arr = adjacent_graph.get(cur_node)
    for node in node_arr:
        # 확인한 노드가 방문기록이 있는지 확인
        if node not in visited_array:
            dfs_recursion_1(adjacent_graph, node, visited_array)
    else:
        return


dfs_recursion_1(graph, 1, visited)  # 1 이 시작노드입니다!
print(visited)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!