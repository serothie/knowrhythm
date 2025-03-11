# Q. 배달의 민족 서버 개발자로 입사했다.
# 상점에서 현재 가능한 메뉴가 ["떡볶이", "만두", "오뎅", "사이다", "콜라"] 일 때, 유저가 ["오뎅", "콜라", "만두"] 를 주문했다.
#
# 그렇다면, 현재 주문 가능한 상태인지 여부를 반환하시오.
# menus = ["떡볶이", "만두", "오뎅", "사이다", "콜라"]
# orders = ["오뎅", "콜라", "만두"]

shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def binary_search(arr, target):
    """이진 탐색 함수: arr에서 target이 있으면 True, 없으면 False 반환"""
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


def is_available_to_order(menus, orders):
    menus.sort()  # 이진 탐색을 위해 정렬

    for order in orders:
        if not binary_search(menus, order):  # 하나라도 찾지 못하면 False 반환
            return False
    else:
        return True  # 모든 주문이 존재하면 True 반환

result = is_available_to_order(shop_menus, shop_orders)
print(result)