# Q. 다음과 같이 영어로 되어 있는 문자열이 있을 때,
# 이 문자열에서 반복되지 않는 첫번째 문자를 반환하시오. 만약 그런 문자가 없다면 _ 를 반환하시오.
# "abadabac" 반복되지 않는 문자는 d, c 가 있지만 "첫번째" 문자니까 d를 반환해주면 됩니다!

#내풀이
#아스키코드를 이용한 인덱스 값으로 활용
def find_not_repeating_first_character(string):
    ascii_array = [0] * 26
    for i in string: # 아스키 코드와 인덱스를 활용하여 반복문자 구분 O(n)
        ascii_array[ord(i) - ord('a')] += 1
    for i in string: # 반복되지 않은 문자 중 가장 첫번째 문자 반환할 수 있도록 함. O(n)
        if ascii_array[ord(i) - ord('a')] == 1:
            return i
    return "_"


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =z 현재 풀이 값 =", result("aaazaaaaca"))