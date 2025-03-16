input = [4, 6, 2, 9, 1]

# 추가되는 것 앞에는 이미 정렬이 되어 있다 따라서 앞에서부터 비교하자
# 최선의 경우에는 $Ω(N)$ 만큼의 시간 복잡도가 걸립니다.
# 입력값이 정렬이 되어있는 편일수록 이득이다

def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        for j in range(i):
            if array[i - j - 1] > array[i - j]:
                array[i - j - 1], array[i - j] = array[i - j], array[i - j - 1]
            else:
                break
    return array

insertion_sort(input)
print(input)

print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ",insertion_sort([5,8,4,7,7]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",insertion_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",insertion_sort([100,56,-3,32,44]))