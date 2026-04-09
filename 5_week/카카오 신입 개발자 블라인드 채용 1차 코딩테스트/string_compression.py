input = "abcabcabcabcdededededede"

"aabbaccc"	# ->
"ababcdcdababcdcd"	# -> 9
"abcabcdede"	# -> 8 )
"abcabcabcabcdededededede"	# -> 14
"xababcdcdababcdcd"	# -> 17
# 내풀이
# 설정 단위로 압축하여 나올 수 있는 문자 길이의 최댓값과 최솟값
# 작은 단위부터 계산 반복하여 해당 단위로 압축한 길이가 그 다음 큰 단위로 압축할 수 있는 길이의 최솟값보다 작다면 거기서 멈춤
# (이 때 최솟값은 갱신되는 형태로)
def string_compression(string):
    # #먼저 설정 단위로 문자열을 나눔
    # 비교 대상 = string[i:i+(설정딘위 + 1)]
    # i = i+(설정딘위 + 1) # 그 다음 값
    # 비교할 대상 = string[i:i+(설정딘위 + 1)]
    # #비교한 값이 같다면 압축 횟수 1 추가, 대신 문자길이는 단위만큼 감소
    # n += 1
    # length -= 설정단위
    # # 그리고 비교대상 변경 없이 그다음 문자 비교, , 압축횟수가 증가할때마다 설정단위만큼 길이 감소,
    # # 비교한 값이 다르다면 압축횟수 변경 없음, 비교대상 변경
    # 비교 대상 = string[i:i+(설정딘위 + 1)]
    #
    # 총길이 = len(str(n)) + string + length
    #
    # # 해당 단위 압축후 길이와 그 전에 측정했던 최소 길이 중 작은 값 비교
    #  더 작은 값의 길이가 다음 단위의 최솟값보다 작다면 멈춤
    #  다음단위의 최솟값 = len(str(입력받은 문자열 // 다음 단위)) + 다음 단위 + (입력받은 문자열 % 다음 단위)
    if string == "":
        return 0

    ###
    unit = 1 # 압축단위
    len_str = len(string)
    cur_min_total_length = len_str
    while unit <= len_str // 2:
        minus_length = 0  # 압축으로 인한 감소되는 문자갯수
        n_length = 0
        i = 0
        while i + unit <= len_str: # 비교대상이 문자열 내부범위에 있어야 함.
            n = 0  # 연속 압축 횟수
            cur_target =  string[i:i + unit] # 비교대상  *이때 파이썬 문법에서는 i + unit이 인덱스범위를 넘어서도 인덱스 에러가 발생하지 않음
            k = i + unit
            while k <= len_str:
                cmp_target = string[k: k + unit] # 비교할 대상
                if cur_target == cmp_target:
                    n += 1
                    minus_length += unit
                    k = k + unit # 다음 비교대상 시작 인덱스
                else:
                    i = k
                    break
            if n != 0: n_length += len(str(n + 1)) # 압축 횟수로 인한 문자열 길이 증가 수 (0개 압축 -> 0, 1~9개 압축 -> 1, 10~99개 -> 2...)
        cur_total_length = n_length + len_str - minus_length # 현재 단위 압축 진행 후 총길이
        cur_min_total_length = min(cur_min_total_length, cur_total_length) # 지금까지 단위 길이 중 최솟값
        unit += 1 #다음 단위
        next_unit_min_total_length = len(str(len_str // unit)) + unit + (len_str % unit) # 다음단위 총길이 최솟값
        if cur_min_total_length <= next_unit_min_total_length:
            return cur_min_total_length

    return cur_min_total_length
### 강의해설
## 모든 경우에서 가장 압축을 많이 시킨 문자열의 길이를 반환해야 함.

print(string_compression(input))  # 14 가 출력되어야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", string_compression("JAAA"))
print("정답 = 9 / 현재 풀이 값 = ", string_compression("AZAAAZDWAAA"))
print("정답 = 12 / 현재 풀이 값 = ", string_compression('BBAABAAADABBBD'))
print("정답 = 9 / 현재 풀이 값 = ", string_compression('ababcdcdababcdcd'))
print("정답 = 8 / 현재 풀이 값 = ", string_compression('abcabcdede'))
print("정답 = 14 / 현재 풀이 값 = ", string_compression('abcabcabcabcdededededede'))
print("정답 = 17 / 현재 풀이 값 = ", string_compression('xababcdcdababcdcd'))
print("정답 = 3 / 현재 풀이 값 = ", string_compression('DDDDDDDDDD'))
print("정답 = 4 / 현재 풀이 값 = ", string_compression('DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD'))