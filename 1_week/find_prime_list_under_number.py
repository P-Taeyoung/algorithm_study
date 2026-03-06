# Q. 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오.
# 소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.
# 20이 입력된다면, 아래와 같이 반환해야 합니다!
# [2, 3, 5, 7, 11, 13, 17, 19]

#내풀이
#1부터 입력받은 숫자까지 반복문을 돌고
#1부터 하나씩 나눠지는 수가 있는지. 즉, 소수에 해당하는지 확인
#이 때, 나눠지는 숫자가 있다면 반복문 중단
def find_prime_list_under_number(number):
    primes = []
    for n_1 in range(2, number):
        is_prime = True #소수인지 아닌지 확인하기 위한 boolean
        for n_2 in range(2, n_1 // 2 + 1): #나누기 연산자 시행시 정수로 인식되게 하기 위해서는 // 즉 몫 연산자를 수행해야 함. 자바의 int / int 와 동일
            if n_1 % n_2 == 0: # n_1 보다 작은 소수들로만 비교해도됨
                is_prime = False # 나눠지는 수가 있다면 소수가 아님
                break
        if is_prime: #반복문을 다 수행했는데도 나눠지는 수가 없다면 소수임
            primes.append(n_1)
    return primes

input = 20
result = find_prime_list_under_number(input)
print(result)

#좀 더 효율적인 방법 :  n_1 보다 작은 소수들로만 비교해도됨. 2와 3로 나누어떨어지지 않는다면 당연히 4, 6, 9로도 나누어 떨어지지 않을 것이기 떄문
def find_prime_list_under_number(number):
    primes = []
    for n_1 in range(2, number):
        is_prime = True #소수인지 아닌지 확인하기 위한 boolean
        for n_2 in primes: #나누기 연산자 시행시 정수로 인식되게 하기 위해서는 // 즉 몫 연산자를 수행해야 함. 자바의 int / int 와 동일
            if n_1 % n_2 == 0: # n_1 보다 작은 소수들로만 비교해도됨
                is_prime = False # 나눠지는 수가 있다면 소수가 아님
                break
        if is_prime: #반복문을 다 수행했는데도 나눠지는 수가 없다면 소수임
            primes.append(n_1)
    return primes

print("--- 개선안 1: 소수들로만 비교하여 소수여부 확인 ---")
input = 22
result = find_prime_list_under_number(input)
print(result)
