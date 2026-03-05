# Q.  다음과 같은 문자열을 입력받았을 때, 어떤 알파벳이 가장 많이 포함되어 있는지 반환하시오.
# (단 최빈값을 가진 알파벳이 여러개일 경우 알파벳 순서가 가장 앞에 위치한 알파벳을 출력하시오)

#내 풀이 1
# 빈 배열을 하나 생성한뒤에 입력받은 배열의 알파벳 값의 아스키 코드를 인덱스 값으로 삼는다.
# 그리고 해당 인덱스 값에 + 1 식 해주어 나중에 가장 큰 값을 찾는다. 이때 같은 값이 있다면 - 1을 반환
# 같은 값이 있는지 판단은 boolean 으로 판단

def find_max_num(arr):
    max_num = -1
    max_num_idx = 0
    for i in range(len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]
            max_num_idx = i
    return max_num_idx

def find_max_occurred_alphabet1(arr):
    ascii_arr = [0] * 26
    for i in arr:
        if i.isalpha():
            ascii_arr[ord(i) - ord('a')] += 1
    max_apb = find_max_num(ascii_arr) # 이전에 작성했던 최댓값 찾는 함수 사용하여 가장 큰 값을 가진 인덱스 찾기
    return chr(max_apb + ord('a'))

result = find_max_occurred_alphabet1
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))

# 내 풀이2
# 반복문을 두 번 돌면서 각 알파벳이 배열에 몇개 있는지 확인

def find_max_occurred_alphabet2(arr):
    max_apb = arr[0]
    max_apb_num = 0
    #첫 번째 알파벳의 개수를 먼저 파악하고 시작
    max_apb = arr[0]
    max_apb_num = 0
    for x in arr:
        if x == max_apb:
            max_apb_num += 1

    is_only_max_apb = True
    for a in arr:
        if max_apb == a: # 만약 최빈값 알파벳이 한번더 나올때는 무시하고 진행 이래야지 무조건 False값이 나오는 것을 방지할 수 있음.
            continue
        this_max_apb_num = 0
        for b in arr:
            if a == b: # 같은 알파벳이 있다면 개수 증가
                this_max_apb_num += 1
        if this_max_apb_num > max_apb_num: # 해당 알파벳의 갯수가 기존에 있던 최빈값보다 많다면 알파벳과 최빈값 변경
            max_apb_num = this_max_apb_num
            max_apb = a
            is_only_max_apb = True # 최빈값 알파벳은 하나인 것을 나타냄
        elif this_max_apb_num == max_apb_num: # 해당 알파벳의 갯수가 기존 최빈값과 같다면
            is_only_max_apb = False # 최빈값 알파벳은 복수인 것을 나타냄

    if is_only_max_apb: # 최빈값 알파벳이 단수라면 바로 반환
        return max_apb

    return -1 # 아니라면 -1 반환

result = find_max_occurred_alphabet2
print("정답 = i 현재 풀이 값 =", result("hello my nameiis dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we lovee algorithm"))
print("정답 = b 현재 풀이 값 =", result("bbest of best youtube"))