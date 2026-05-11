# 일단 식에 나오는 숫자들은 전부 제외
# 자릿수가 넘어갈 때 숫자가 어떻게 되는지 확인해야 함. 십의 단위가 바뀔 때 값이 있다면 몇 진법인지 알아낼 수 있음.
# 두 숫자를 더했을 때 십진법의 숫자와 다르다면 해당 식을 통해 몇 진법인지 알 수 있음.
# 두 숫자를 더했을 때 (자리수가 안바뀐다고 가정할 때) 십진법의 숫자와 같다면 해당 식에서 나온 최고 숫자 이하 진법은 아님 ex) 2 + 4 = 6 라면 6 이하 진법은 아님.
import re

def solution(expressions):
    max_digit = 0
    for expression in expressions:
        nums = re.findall(r'\d', expression)
        max_digit = max(max_digit, int(sorted(nums)[-1]))

    possible_bases = list(range(max_digit + 1, 10))
    print(possible_bases)

    for expression in expressions:
        if "X" not in expression:
            exp = expression.split()
            op = exp[1]
            for base in possible_bases[:]: # 시행착오 : 지우면서 돌면 안됨
                a_num = int(exp[0], base)
                b_num = int(exp[2], base)
                result = int(exp[-1], base)
                print(base ,"진법일 때 ",a_num, op, b_num,  "=",result)
                if op == "+":
                    if a_num + b_num != result:
                        possible_bases.remove(base)
                elif op == "-":
                    if a_num - b_num != result:
                        possible_bases.remove(base)

    print(possible_bases)

    answer = []
    for expression in expressions:
        if "X" in expression:
            exp = expression.split()
            op = exp[1]
            result = set()
            for base in possible_bases:
                a_num = int(exp[0], base)
                b_num = int(exp[2], base)
                if op == "+":
                    result.add(convert_to_n(a_num + b_num, base))
                elif op == "-":
                    result.add(convert_to_n(a_num - b_num, base))
            if len(result) > 1:
                new_answer = expression.replace("X", "?")
            else:
                new_answer = expression.replace("X", next(iter(result)))
            answer.append(new_answer)


    return answer



def convert_to_n(num, n):
    if num == 0:
        return "0"

    digits = "012345678"
    result = ""

    while num > 0:
        # num을 n으로 나눈 몫과 나머지를 동시에 구함
        num, remainder = divmod(num, n)
        # 나머지를 결과 앞에 붙임 (역순으로 읽는 효과)
        result = digits[remainder] + result

    return result


print(solution(["14 + 3 = 17", "13 - 6 = X", "51 - 5 = 44"]))
print(solution(["1 + 1 = 2", "1 + 3 = 4", "1 + 5 = X", "1 + 2 = X"]))
print(solution(["10 - 2 = X", "30 + 31 = 101", "3 + 3 = X", "33 + 33 = X"]))
print(solution(["2 - 1 = 1", "2 + 2 = X", "7 + 4 = X", "5 - 5 = X"]	))
print(solution(["2 - 1 = 1", "2 + 2 = X", "7 + 4 = X", "8 + 4 = X"]))