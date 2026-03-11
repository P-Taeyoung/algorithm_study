# Q. 음이 아닌 정수들로 이루어진 배열이 있다. 이 수를 적절히 더하거나 빼서 특정한 숫자를 만들려고 한다.
# 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들기 위해서는 다음 다섯 방법을 쓸 수 있다.
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# 사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target_number이 매개변수로 주어질 때
# 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 반환하시오.

numbers = [1, 1, 1, 1, 1]
target_number = 3


# 내풀이:
# 다음 수로 넘어갈 때 경우의 수는 2가지 더하거나 빼거나
# 이 모든 경우의 수를 구해 원하는 값이 나오는 경우만 더하여 합계를 구하기
# 탈출 조건: 배열 끝에 도달했을 때

def get_answer(array, sum, target, idx):
    count = 0
    plus_sum = sum + numbers[idx]
    minus_sum = sum - numbers[idx]
    if idx == len(array) - 1: #배열 끝에 도달했을 때 빼거나 더했을 때 값이 target값과 같다면 해당 경우의 수를 count
        if plus_sum == target:
            count += 1
        if minus_sum == target:
            count += 1
        return count

    # 더하는 경우, 빼는 경우
    count = get_answer(array, plus_sum, target, idx + 1) + get_answer(array, minus_sum, target, idx + 1)
    return count

def get_count_of_ways_to_target_by_doing_plus_or_minus_1(array, target):
    # 구현해보세요!
    return get_answer(array, 0, target, 0)

# 개선안
# 개념은 똑같음 다만 코드 구조가 살짝 다름
def get_count_of_ways_to_target_by_doing_plus_or_minus_2 (array, target):
    all_ways = []

    def get_all_ways_by_doing_plus_or_minus(array, current_index, current_sum):
        if current_index == len(array):
            all_ways.append(current_sum)
            return

        get_all_ways_by_doing_plus_or_minus(array, current_index + 1, current_sum + array[current_index])
        get_all_ways_by_doing_plus_or_minus(array, current_index + 1, current_sum - array[current_index])

    get_all_ways_by_doing_plus_or_minus(array, 0, 0) # 모든 경우의 수의 값을 구함
    print(all_ways)
    target_count = 0

    for way in all_ways: # 모든 경우의 수 값중에 target과 일치하는 값 탐색
        if target == way:
            target_count += 1

    return target_count




print(get_count_of_ways_to_target_by_doing_plus_or_minus_1(numbers, target_number))  # 5를 반환해야 합니다!
print(get_count_of_ways_to_target_by_doing_plus_or_minus_2(numbers, target_number))  # 5를 반환해야 합니다!
