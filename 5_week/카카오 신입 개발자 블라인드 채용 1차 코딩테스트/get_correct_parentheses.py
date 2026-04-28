from collections import deque

balanced_parentheses_string = "()))((()"

# 내풀이
# 문제 그대로 풀 수 있도록 함. 다만 풀기 쉽도록 각각의 기능에 맞춰 함수를 정의
# 올바른 괄호 문자열인지 판별하는 함수
# 균형잡힌 괄호 문자열 u, v로 나누는 함수
# u 가 올바른 괄호 문자열이 아닐때 기능하는 함수
def get_correct_parentheses (balanced_parentheses_string):
    if balanced_parentheses_string == "":
        return ""

    u, v = split_balanced_parentheses(balanced_parentheses_string)

    if is_correct_parentheses(u):
        v = get_correct_parentheses(v)
        return u + v
    else:
        u = become_correct_parentheses(u)
        return "(" + get_correct_parentheses(v) + ")" + u
    return

def split_balanced_parentheses (string):
    u = ""
    v = ""
    left_cnt = 0
    right_cnt = 0
    queue = deque()
    for char in string:
        queue.append(char)

    while queue:
        char = queue.popleft()
        if char == "(":
            left_cnt += 1
            u += char
        else:
            right_cnt += 1
            u += char
        if left_cnt == right_cnt:
            break

    if queue:
        while queue:
            char = queue.popleft()
            v += char

    return u, v

def is_correct_parentheses (u):
    stack = []
    for char in u:
        if char == "(":
            stack.append(char)
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False

    return True

def become_correct_parentheses (string):
    str = string[1:-1]
    u = ""
    for char in str:
        if char == "(":
            u += ")"
        else:
            u += "("
    return u



print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!

print("정답 = (((()))) / 현재 풀이 값 = ", get_correct_parentheses(")()()()("))
print("정답 = ()()( / 현재 풀이 값 = ", get_correct_parentheses("))()("))
print("정답 = ((((()())))) / 현재 풀이 값 = ", get_correct_parentheses(')()()()(())('))