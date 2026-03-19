array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]

#내풀이
#받은 2개 배열의 수만큼 반복 (어떠한 상황이라도 무조건 두 배열 합친길이만큼 반복하게 됨)
#각 배열 원소값을 비교후 작은 값을 새로운 배열에 추가
#값이 빠진 배열은 그 다음 인덱스로 이동하여 비교
#더이상 이동할 인덱스가 없다면 나머지 배열의 원소값은 차례대로 추가
def merge(array1, array2):
    # 이 부분을 채워보세요!
    n = len(array1) + len(array2)
    answer_array = []
    arr1_idx = 0
    arr2_idx = 0
    for i in range(n):
        if arr1_idx >= len(array1):
            answer_array.append(array2[arr2_idx])
            arr2_idx += 1
        elif arr2_idx >= len(array2):
            answer_array.append(array1[arr1_idx])
            arr1_idx += 1
        elif array1[arr1_idx] < array2[arr2_idx]:
            answer_array.append(array1[arr1_idx])
            arr1_idx += 1
        else:
            answer_array.append(array2[arr2_idx])
            arr2_idx += 1
    return answer_array


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge([-7, -1, 9, 40], [5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge([-1,2,3,5,40], [10,78,100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge([-1,-1,0], [1, 6, 9, 10]))