from collections import deque

# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}


def bfs_queue(adj_graph, start_node):
    # 구현해보세요!
    # 큐 생성 후 시작 노드를 삽입
    queue = deque([start_node])
    # 방문 여부를 확인할 배열
    visited = []

    while queue:
        # 큐에서 노드 추출
        node = queue.popleft()
        # 방문 배열에 저장
        visited.append(node)
        # 인접 노드 중에서 방문한 적이 없는 노드를 큐에 삽입
        for adjacent_node in adj_graph[node]:
            if adjacent_node not in visited:
                queue.append(adjacent_node)

    return visited


print(bfs_queue(graph, 1))  # 1 이 시작노드입니다!
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!