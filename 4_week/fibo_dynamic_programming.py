input = 50

# memo 라는 변수에 Fibo(1)과 Fibo(2) 값을 저장해놨습니다!
memo = {
    1: 1,
    2: 1
}


def fibo_dynamic_programming(n, fibo_memo):
    # 구현해보세요!
    # 메모에 이미 해당값이 있다면 반환 (같은 계산을 반복하지 않게 하기 위해)
    if n in fibo_memo.keys():
        return fibo_memo[n]
    # 없다면 재귀함수 호출해야 함
    else:
        fibo_memo[n] = fibo_dynamic_programming(n - 2, fibo_memo) + fibo_dynamic_programming(n - 1, fibo_memo)
        return fibo_memo[n]
    # 반복되는 값을 반복 계산하지 않고 메모에 있는 값을 바로 가져와 계산할 수 있기 때문에 연산이 감소함.

print(fibo_dynamic_programming(input, memo))