import re
from itertools import permutations
# 문제 풀이 방식
# 1) 우선 *를 찾습니다.
# 2) * 기준으로 앞 뒤의 숫자들을 연산한 뒤 연산 결과를 제외한 연산자와 숫자들은 제거합니다.
# 3) 그리고 다시 *를 찾고, 없다면 다음 연산자를 찾습니다.
#
# 1) 런타임의 값들로 보면 다음과 같습니다.
# 지금 expression 변수가 다음과 같이 되어 있습니다.
# ["100", "-", "200", "*", "300", "-", "500", "+", "20"]
#
# 2) 그러면 여기서 *를 찾습니다.
# 그리고 앞 뒤에 있는 문자열인 "200"과 "300"을 연산합니다.
# 숫자 60000 이 됩니다.
#
# 3) 그리고 "200", "*", "300"을 없애고 60000을 넣습니다.
# 그러면 expression 변수가 다음과 같이 되어 있습니다.
# ["100", "-", "60000", "-", "500", "+", "20"]

def solution(expression):
    answer = 0

    operation_list = list()
    if '*' in expression:
        operation_list.append('*')
    if '+' in expression:
        operation_list.append('+')
    if '-' in expression:
        operation_list.append('-')

    operation_permutations = list(permutations(operation_list))
    expression = re.split('([^0-9])', expression)

    for operation_permutation in operation_permutations:
        copied_expression = expression[:]
        for operator in operation_permutation:
            while operator in copied_expression:
                op_idx = copied_expression.index(operator)
                cal = str(
                    eval(copied_expression[op_idx - 1] + copied_expression[op_idx] + copied_expression[op_idx + 1])
                )

                copied_expression[op_idx - 1] = cal
                copied_expression = copied_expression[:op_idx] + copied_expression[op_idx + 2:]

        answer = max(answer, abs((int(copied_expression[0]))))

    return answer