# 그래프 형태를 만드는 방법
# y갑을 기준으로 내림차순
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(node, data):
    if node is None:
        return Node(data)
    if data[1][0] < node.data[1][0]:
        node.left = insert(node.left, data)
    else:
        node.right = insert(node.right, data)

    return node


def find_preorder(root):
    answer = []
    if not root:
        return answer
    stack = [root]

    while stack:
        node = stack.pop()
        answer.append(node.data[0])

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)
    return answer


def find_postorder(root):
    if not root:
        return []
    stack = [root]
    answer = []

    while stack:
        node = stack.pop()
        answer.append(node.data[0])

        if node.left:
            stack.append(node.left)

        if node.right:
            stack.append(node.right)

    return answer[::-1]


def solution(nodeinfo):
    node_dict = {}
    for i, node in enumerate(nodeinfo):
        node_dict[i + 1] = node

    sorted_nodes = sorted(node_dict.items(), key=lambda x: -x[1][1])

    root = None
    for node in sorted_nodes:
        root = insert(root, node)


    return [find_preorder(root), find_postorder(root)]


print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))
