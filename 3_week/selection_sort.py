# Q. 다음과 같이 숫자로 이루어진 배열이 있을 때, 오름차순으로 선택 정렬을 이용해서 정렬하시오.

input = [4, 6, 2, 9, 1]

# 내풀이
# 전체 배열을 다 탐색하여 가장 작은 값을 찾음
# 가장 작은 값을 맨 앞으로 옮김.
# 그 후 가장 첫번째 인덱스를 제외하고 다시 위 과정을 반복
def selection_sort(array):
    # 이 부분을 채워보세요!
    for i in range(len(array) - 1):
        min_idx = i
        for k in range(i + 1, len(array)):
             if array[k] < array[min_idx]:
                min_idx = k
        array[i], array[min_idx] = array[min_idx], array[i]
    return array


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",selection_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",selection_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",selection_sort([100,56,-3,32,44]))