array = [5, 3, 2, 1, 6, 8, 7, 4]

# 내풀이
# 배열을 2등분 한 후
# 정렬합을 구함 (merge함수 이용)
# 탈출 조건은 원소가 1개밖에 없을 때
def merge_sort(array):
    # => N을 1이 될 때까지 계속 2로 나누는 과정 따라서 O(logN)의 시간복잡도를 가지게 됨.
    # 이를 정렬과 합치게 되면 병합 정렬의 총 시간복잡도는 O(NlogN)임!!!
    if len(array) <= 1:
        return array
    new_array = merge(merge_sort(array[:len(array)//2]), merge_sort(array[len(array)//2:]))
    return new_array

def merge(array1, array2):  # -> O(N)의 시간복잡도
    result = []
    array1_index = 0
    array2_index = 0
    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1

    if array1_index == len(array1):
        while array2_index < len(array2):
            result.append(array2[array2_index])
            array2_index += 1

    if array2_index == len(array2):
        while array1_index < len(array1):
            result.append(array1[array1_index])
            array1_index += 1

    return result

print(merge_sort(array))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge_sort([-7, -1, 9, 40, 5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge_sort([-1, 2, 3, 5, 40, 10, 78, 100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge_sort([-1, -1, 0, 1, 6, 9, 10]))