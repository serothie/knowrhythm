seat_count = 9
vip_seat_array = [4, 7]

# 이 문제의 핵심은 변경 가능한 좌석들의 규칙을 발견하는 것입니다.
#
# 규칙을 우선 숫자를 써보면서 발견해보겠습니다!
#
# 좌석 [1, 2] 를 옮겨본다고 해보겠습니다.
# 가능한 경우는 [1, 2] [2, 1] 총 2개 입니다.
#
# 좌석 [1, 2, 3] 를 옮겨본다고 해보겠습니다.
# 가능한 경우는 [1, 2, 3] [2, 1, 3] [1, 3, 2] 총 3개 입니다.
#
# 좌석 [1, 2, 3, 4] 를 옮겨본다고 해보겠습니다.
# 가능한 경우는 [1, 2, 3, 4] [1, 2, 4, 3] [1, 3, 2, 4] [2, 1, 3, 4] [2, 1, 4, 3] 총 5개 입니다.
# 피보나치네?

seat_count = 9
vip_seat_array = [4, 7]

# 예전에 만들었던 fibo_dynamic_programming 에서 가져오면 됩니다!
memo = {
    1: 1,  # 이 문제에서는 Fibo(1) = 1, Fibo(2) = 2 로 시작합니다!
    2: 2
}


def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo
    return nth_fibo


def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    all_ways = 1
    current_index = 0
    for fixed_seat in fixed_seat_array:
        fixed_seat_index = fixed_seat - 1
        count_of_ways = fibo_dynamic_programming(fixed_seat_index - current_index, memo)
        all_ways *= count_of_ways
        current_index = fixed_seat_index + 1

    count_of_ways = fibo_dynamic_programming(total_count - current_index, memo)
    all_ways *= count_of_ways
    return all_ways


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))

print("정답 = 4 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(9,[2,4,7]))
print("정답 = 26 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(11,[2,5]))
print("정답 = 6 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(10,[2,6,9]))