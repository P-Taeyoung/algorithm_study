# Q.
# 1. 입력으로 소문자의 알파벳 순으로 정렬된 문자열이 입력됩니다.
# 2. 각 알파벳은 중복이 가능합니다.
# 3. 중간에 없는 알파벳이 있을 수도 있습니다.
#
# 입,출력 예시와 같이 입력 문자열에 나타나는 각 알파벳의 종류,갯수를 요약하여 나타내시오.
# 문제의 번호별 조건에 대한 입력 예시와 출력
# Ex 1)
# abc 	# a1/b1/c1
#
# Ex 2-1)
# aaabbbc	# a3/b3/c1
#
# Ex 2-2)
# abbbc	# a1/b3/c1
#
# Ex 3-1)
# ahhhhz	# a1/h4/z1
#
# Ex 3-2)
# acccdeee	# a1/c3/d1/e3

#내풀이
#특징 : 문자가 abc 순으로 정렬되어 있다는 점.
#문자가 바뀌는 순간에 해당 문자와
def summarize_string(input_str):
    current_chr = input_str[0]
    current_chr_sum = 0
    sum_str = []
    for chr in input_str:
        if chr == current_chr:
            current_chr_sum += 1
        else:
            sum_str.append(f"{current_chr}{current_chr_sum}")
            current_chr_sum = 1
            current_chr = chr

    sum_str.append(f"{current_chr}{current_chr_sum}")

    answer = "/".join(sum_str)
    return answer

# 이 부분을 채워보세요!


input_str = "acccdeee"

print(summarize_string(input_str))

#정답 풀이
def summarize_string(target_string):
    # 이 부분을 채워보세요!
    n = len(target_string)
    count = 0
    result_str = ''

    for i in range(n - 1):
        if target_string[i] == target_string[i + 1]:
            count += 1
        else:
            result_str += target_string[i] + str(count + 1) + '/'
            count = 0

    result_str += target_string[n - 1] + str(count + 1)

    return result_str


input_str = "acccdeee"

print(summarize_string(input_str))