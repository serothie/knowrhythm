import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30

# 1. 현재 재고의 상태에 따라 최곳값을 받아야 된다. (동적 변경 상황)
# 2. 제일 많은 값만 가져가면 된다.
# => maxHeap

# stock 이 비면 공장이 멈추기 때문에 stock 이 떨어지기 전까지의 공급량들 중에서 가장 큰 값을 넣어야 합니다!!!!!

def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    # 풀어보세요!
    result = 0
    last_added_date_index = 0
    max_heap = []

    while stock <= k:
        while last_added_date_index < len(dates) and dates[last_added_date_index] <= stock : # 인덱스 검사가 먼저있어야 에러가 안남
            heapq.heappush(max_heap, supplies[last_added_date_index] * -1)
            last_added_date_index += 1
        result += 1
        heappop = heapq.heappop(max_heap)
        stock += -heappop

    return result


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
print("정답 = 2 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15], [20, 5, 10], 30))
print("정답 = 4 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15, 20], [20, 5, 10, 5], 40))
print("정답 = 1 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(2, [1, 10], [10, 100], 11))