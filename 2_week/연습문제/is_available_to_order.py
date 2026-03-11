# Q. 배달의 민족 서버 개발자로 입사했다.
# 상점에서 현재 가능한 메뉴가 ["떡볶이", "만두", "오뎅", "사이다", "콜라"] 일 때, 유저가 ["오뎅", "콜라", "만두"] 를 주문했다.
# 그렇다면, 현재 주문 가능한 상태인지 여부를 반환하시오.
# menus = ["떡볶이", "만두", "오뎅", "사이다", "콜라"]
# orders = ["오뎅", "콜라", "만두"]

shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]

# 내풀이:
# orders에 있는 메뉴가 menus에 있는지 비교
def is_available_to_order_1(menus, orders):
    # 이 부분을 채워보세요!
    for order in orders:
        for menu in menus:
            if order == menu:
                break
        else:
            return False
    return True

# 개선안
# set, not in 함수를 이용
def is_available_to_order_2(menus, orders):
    menus_set = set(menus) # O(N)
    for order in orders: # O(M)
        if order not in menus_set: # O(1)
            return False

    # => O(N) + O(M) * O(1) = O(N + M)
    return True

result = is_available_to_order_1(shop_menus, shop_orders)
result1 = is_available_to_order_2(shop_menus, shop_orders)
print(result)
print(result1)