# Q. 음이 아닌 정수들로 이루어진 배열이 있다. 이 수를 적절히 더하거나 빼서 특정한 숫자를 만들려고 한다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들기 위해서는 다음 다섯 방법을 쓸 수 있다.
#
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
#
# 사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target_number이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 반환하시오.
# numbers = [1, 1, 1, 1, 1]
# target_number = 3

# 정말 잘 모르겠는 경우 예제를 만들어서 모든 경우의 수 따져보자 규칙이 보이지 않을까??? 근데 없다면??? 진짜 없을 수 있다..

# 즉, 하나씩 원소를 추가할 때마다 새로 추가된 원소를 더하고 빼는 경우의 수를 추가하면 됩니다. 즉 재귀쓰..

numbers = [1, 1, 1, 1, 1]
target_number = 3


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    all_ways = []

    def get_all_ways_by_doing_plus_or_minus(array, current_index, current_sum):
        if current_index == len(array):
            all_ways.append(current_sum)
            return

        get_all_ways_by_doing_plus_or_minus(array, current_index + 1, current_sum + array[current_index])
        get_all_ways_by_doing_plus_or_minus(array, current_index + 1, current_sum - array[current_index])

    get_all_ways_by_doing_plus_or_minus(array, 0, 0)
    target_count = 0

    for way in all_ways:
        if target == way:
            target_count += 1

    return target_count

print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!