finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


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


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)