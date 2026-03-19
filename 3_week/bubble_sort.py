input = [4, 6, 2, 9, 1]

# 내풀이
# 배열 끝에서부터 차례대로 정렬되어야 함.
# 정렬하기 위한 비교가 반복될 때 한 번 반복이 끝나면 맨 끝에는 이미 정렬이 되었기 떄문에 비교 범위에서 제외해야 함.
def bubble_sort(array):
    # 이 부분을 채워보세요!
    for i in range(len(array) - 1): # 5개 원소가 있을 때 비교횟수는 4번임
        for k in range(len(array) - i - 1):
            if array[k] > array[k + 1]:
                array[k], array[k + 1] = array[k + 1], array[k]
    return array

# => O(N^2) 시간 복잡도를 가짐. 
bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",bubble_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",bubble_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",bubble_sort([100,56,-3,32,44]))