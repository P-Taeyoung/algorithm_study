# 연산자 우선순위를 정한뒤
# 절대값 기준으로 가장 큰 값이 무엇인지 반환

# 우선순위 조합을 정한뒤
# 각 조합으로 계산했을 때 가장 큰 값을 구하면 될 것

# 계산을 하는 법
# 우선순위가 낮은 연산기호 기준으로 순서대로 split을 해서 가장 안쪽부터 계산을 하면 될듯
# ex) + > - > * 일 때, "50*6-3*2" -> "50", "6-3", "2" ->  "50", "6", "3", "2" ->  "50", "6", "3", "2" -> "6", "3"부터 계산
# 주의할 점 + 으로 split을 했을 때는 값이 변하지 않음. 따라서 그때는 + 를 계산하면 안됨. 즉 중간에 포함되지 않은 연산자가 있을 경우 계산을 하지 않도록 해야 함.
from itertools import permutations

def solution(expression):
    maximize = 0
    operator_combs = list(permutations(["*", "+", "-"], 3))
    for operator_comb in operator_combs:
        print(operator_comb)
        cum = abs(calculate(expression, operator_comb, 0))
        maximize = max(maximize, cum)

    return maximize

def calculate(expression, operators, i):
    print("들어온 수식: ", expression, "단계: ", i)
    if expression.isdigit():
        print("score: ", int(expression))
        return int(expression)

    new_expressions = expression.split(operators[i])

    answer = calculate(new_expressions[0], operators, i + 1)
    if operators[i] == "*":
        for j in range(1, len(new_expressions)):
            answer *= calculate(new_expressions[j], operators, i + 1)
            print(answer)
    elif operators[i] == "+":
        for j in range(1, len(new_expressions)):
            answer += calculate(new_expressions[j], operators, i + 1)
            print(answer)
    elif operators[i] == "-":
        for j in range(1, len(new_expressions)):
            answer -= calculate(new_expressions[j], operators, i + 1)
            print(answer)


    return answer


print(solution("50*6-3*2"))
