# Q. 배달의 민족 서버 개발자로 입사했다.
# 상점에서 현재 가능한 메뉴가 ["떡볶이", "만두", "오뎅", "사이다", "콜라"] 일 때, 유저가 ["오뎅", "콜라", "만두"] 를 주문했다.
#
# 그렇다면, 현재 주문 가능한 상태인지 여부를 반환하시오.
# menus = ["떡볶이", "만두", "오뎅", "사이다", "콜라"]
# orders = ["오뎅", "콜라", "만두"]

shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False  # 못 찾았을 경우 False

# 시간복잡도는 (M + N) * logN
# def is_available_to_order(menus, orders):
#     menus.sort()
#
#     for order in orders:
#         if not binary_search(menus, order):
#             return False
#     else:
#         return True

def is_available_to_order(menus, orders):
    menus_set = set(menus) # 시간 복잡도 N
    for order in orders: # 시간 복잡도 M
        if order not in menus_set: # 시간 복잡도 1
            return False
    return True

result = is_available_to_order(shop_menus, shop_orders)
print(result)