input = [4, 6, 2, 9, 1]

# def bubble_sort(array):
#     # 이 부분을 채워보세요!
#     swap_count = 0
#     for i in range(len(array) - 1):
#         if array[i] > array[i + 1]:
#             array[i], array[i + 1] = array[i + 1], array[i]
#             swap_count += 1
#
#     if swap_count == 0:
#         return array
#     else:
#         return bubble_sort(array)

def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

bubble_sort(input)
print(input)



print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",bubble_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",bubble_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",bubble_sort([100,56,-3,32,44]))