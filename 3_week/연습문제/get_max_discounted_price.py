# Q.
# 다음과 같이 숫자로 이루어진 배열이 두 개가 있다.
# 하나는 상품의 가격을 담은 배열이고, 하나는 쿠폰을 담은 배열이다.
# 쿠폰의 할인율에 따라 상품의 가격을 할인 받을 수 있다.
# 이 때, 최대한 할인을 많이 받는다면 얼마를 내야 하는가?
# 단, 할인쿠폰은 한 제품에 한 번씩만 적용 가능하다.
# [30000, 2000, 1500000] # 상품의 가격
# [20, 40]               # 쿠폰, 할인율의 단위는 % 입니다.

hop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]

#내풀이
#제일 가격이 높은 것에는 제일 할인률이 높은 쿠폰이 적용되어야 함.
#따라서 정렬후 적용이 될 수 있도록 함.
def get_max_discounted_price_1(prices, coupons):
    # 이 곳을 채워보세요!
    # 1. 정렬처리 (내림차순으로 정렬)
    prices.sort(reverse=True)
    coupons.sort(reverse=True)

    # 2. 가장 큰 값과 가장 큰 쿠폰이 적용될 수 있도록 함
    # (이 때, 상품이 남았는데 쿠폰이 먼저 소진된다면 가격 그대로 적용될 수 있도록 함)
    sum = 0
    for i in range(0, len(prices)):
        if i < len(coupons):
            sum += prices[i] * (100 - coupons[i]) // 100
        else:
            sum += prices[i]

    return sum


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price_1([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price_1([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price_1([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price_1([20000, 100000, 1500000], [10, 10, 10]))