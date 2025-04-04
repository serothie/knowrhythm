from json.encoder import INFINITY


def find_max_num(array):
    max_number = array[0]
    for number in array:
        max_number = max(max_number, number)
    return max_number


print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))

# def find_max_num(array):
#     max_num = array[0]
#     for num in array:
#         if num > max_num:
#             max_num = num
#     return max_num