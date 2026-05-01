# 연산자 우선순위를 정한뒤
# 절대값 기준으로 가장 큰 값이 무엇인지 반환

# 우선순위 조합을 정한뒤
# 각 조합으로 계산했을 때 가장 큰 값을 구하면 될 것

# 계산을 하는 법
# 우선순위가 낮은 연산기호 기준으로 순서대로 split을 해서 가장 안쪽부터 계산을 하면 될듯
# ex) + > - > * 일 때, "50*6-3*2" -> "50", "6-3", "2" ->  "50", "6", "3", "2" ->  "50", "6", "3", "2" -> "6", "3"부터 계산
# 주의할 점 + 으로 split을 했을 때는 값이 변하지 않음. 따라서 그때는 + 를 계산하면 안됨. 즉 중간에 포함되지 않은 연산자가 있을 경우 계산을 하지 않도록 해야 함.
# 분할정복으로 품
# Step 1. 가장 단순한 경우를 생각한다 (Base Case)"수식에 연산자가 없고 숫자만 있다면?"
# • 결론: 계산할 것이 없습니다. 그 숫자 자체가 결과값입니다.
# • 코드 반영: if expression.isdigit(): return int(expression)
# Step 2. 한 단계 위를 생각한다 (Recursive Step)"연산자가 딱 하나($10 + 20$) 있다면?"
# • 결론: +를 기준으로 왼쪽(10)과 오른쪽(20)을 각각 계산(Step 1 수행)한 뒤, 두 결과를 더합니다.
# Step 3. 일반화하여 추상화한다 (Generalization)"우선순위가 낮은 연산자가 중간에 끼어 있다면?"
# • 가정: 나는 현재 연산자보다 우선순위가 높은 애들을 계산하는 방법을 이미 알고 있다고 칩니다. (재귀의 마법)
# • 전략:
#     1. 현재 가장 우선순위가 낮은 연산자(예: +)를 찾습니다.
#     2. 그 연산자를 기준으로 수식을 크게 덩어리로 쪼갭니다. (A + B + C)
#     3. 쪼개진 각 덩어리($A, B, C$)는 나보다 우선순위가 높은 연산자들로만 이루어져 있습니다.
#     4. 이 덩어리들을 다시 '계산 함수'에 던져서 결과값을 받아온 뒤, 마지막에 현재 연산자(+)로 합칩니다.
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
    #연산자가 없다면 숫자그대로 반환
    if expression.isdigit():
        print("score: ", int(expression))
        return int(expression)

    new_expressions = expression.split(operators[i])
    # 연산자 앞부분 구하기
    answer = calculate(new_expressions[0], operators, i + 1)
    # 연산자 뒷부분 구하기
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
