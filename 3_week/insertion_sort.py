# Q. 다음과 같이 숫자로 이루어진 배열이 있을 때, 오름차순으로 삽입 정렬을 이용해서 정렬하시오.


input = [4, 6, 2, 9, 1]

# 내풀이
# 범위를 하나씩 늘려가면서 앞선 원소와 비교하여 올바른 위치에 삽입
def insertion_sort(array):
    # 이 부분을 채워보세요!
    for i in range(1, len(array)):
        for j in range(i - 1, -1, -1):
            if array[j] > array[i]:
                array[i], array[j] = array[j], array[i]
                i -= 1 # 자리를 바꾼 인덱스 값을 따라가야 함.
            else:
                break # 앞 인덱스의 값이 이미 작다면 더 이상 비교할 필요가 없음. -> 이미 앞 인덱스들은 정렬되어있기 떄문에
                      # 시간 복잡도가 그나마 좀 더 줄어들 수 있음. -> Big Omega 의 경우 N 만큼의 시간이 걸림.
    return array


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ",insertion_sort([5,8,4,7,7]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",insertion_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",insertion_sort([100,56,-3,32,44]))