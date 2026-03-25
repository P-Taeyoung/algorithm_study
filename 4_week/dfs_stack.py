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


def dfs_stack(adjacent_graph, start_node):
    # 구현해보세요!
    # 첫번째 방문 노드를 스택에 삽입
    stack = [start_node]
    visited = []
    while stack:
        # 스택 특성을 이용하여 마지막 삽입 원소를 빼냄
        node = stack.pop()
        # 빼낸 노드는 방문상태로 변경
        visited.append(node)
        for adjacent_node in adjacent_graph[node]:
            # 인접 노드에서 방문하지 않은 노드는 스택에 삽입
            if adjacent_node not in visited:
                stack.append(adjacent_node)
    return visited


print(dfs_stack(graph, 1))  # 1 이 시작노드입니다!
# [1, 9, 10, 5, 8, 6, 7, 2, 3, 4] 이 출력되어야 합니다!