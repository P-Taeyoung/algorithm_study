finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_existing_target_number_binary(target, array):
    # 구현해보세요
    current_min = 0
    current_max = len(array) - 1
    current_index = (current_min + current_max) // 2
    count = 0

    while current_min <= current_max:
        count += 1
        if array[current_index] == target:
            print(count)
            return True
        elif array[current_index] < target:
            current_min = current_index + 1
        elif array[current_index] > target:
            current_max = current_index - 1
        current_index = (current_min + current_max) // 2

    return False

def is_exist_target_number_binary_1(target, array):
    # 내풀이
    # 정렬 후 이진탐색
    for i in range(0, len(array)):
        for k in range(i + 1, len(array)):
            if array[i] > array[k]:
                tmp = array[i]
                array[i] = array[k]
                array[k] = tmp
    else:
        print(array)

    return is_existing_target_number_binary(target, array)

# 무작위로 정렬되어 있는 경우 이진 탐색을 사용하기 어려움.
result = is_exist_target_number_binary_1(finding_target, finding_numbers)
print(result)