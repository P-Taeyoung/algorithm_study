# 97 + 98 + 99 + 100... 122 = x
# 1 + 2 + 3 + 4 + 5 에서 2, 3을 빼고 난 후 3번째 자리는 5 임 즉 두개 원소가 빠졌을 때 -2 =>
# 원래 구하려던 곳의 숫자값을 구한뒤 구하려던 곳 포함하여 이전 원소가 몇개 빠졌는지 구하고 원래 구하려던 곳의 숫자값에 더하면 답을 구할 수 있음.
# 이 때 25가 넘어가면 단위가 커진다는 것을 인지해야 함. 즉 z -> aa 로 넘어가는 경우를 잘 계산해야 함.

def solution(n, bans):
    init_n = n
    cnt = 0
    sorted_bans = sorted(bans, key=lambda t: (len(t), t))
    # 시행착오 2: 1 순위: 글자길이 2순위: 알파벳 순대로 정렬을 먼저해야 올바르게
    # n 보다 앞선 글자 갯수를 구할 수 있음. 만약 정렬하지 않으면 뒤에 글자가 n 보다 앞서서 빠지는 것이 반영이 안된채 앞순서 글자를 넘어갈 수 있기 때문임.

    print(sorted_bans)
    # sorted_targets = sorted(targets, key=lambda t: t[1])

    for ban in sorted_bans:
        ban_to_num = alphabet_to_int(ban)
        print(ban_to_num)
        if ban_to_num <= n:
            n += 1 # =>  시행 착오 1: 앞에서 빠진 글자 수에 따라 원래는 n 번째 이후였던 글자가 n 번째 내로 들어올 수 있기 때문

    return int_to_alphabet(n)

# 알파벳으로 구성된 26진법을 10진법으로 변환하는 함수
def alphabet_to_int(string):
    res = 0
    for char in string:
        res = res * 26 + (ord(char) - ord('a') + 1)
    return res

#
def int_to_alphabet(n):
    res = ''
    while n > 0:
        n, remainder = divmod(n - 1, 26)# 몫과 나머지를 동시에 반환해주는 함수 divmod(대상 숫자, 나눌 숫자)
        res = chr(ord('a') + remainder) + res
    return res


print(solution(7388, ["gqk", "kdn", "jxj", "jxi", "fug", "jxg", "ewq", "len", "bhc"]))
print(solution(30,	["d", "e", "bb", "aa", "ae"]))

#시행착오-1 정렬해야 함.