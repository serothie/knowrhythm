from curses.ascii import isalpha
from operator import indexOf


def find_max_occurred_alphabet(string):
    # 이 부분을 채워보세요!
    alphabet_occurrence_array = [0] * 26
    for char in string:
        if not isalpha(char):
            continue
        alphabet_occurrence_array[ord(char) - 97] += 1
    return chr(alphabet_occurrence_array.index(max(alphabet_occurrence_array)) + 97)


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))

# def find_max_occurred_alphabet(string):
#     alphabet_occurrence_array = [0] * 26
#
#     for char in string:
#         if not char.isalpha():
#             continue
#         arr_index = ord(char) - ord('a')
#         alphabet_occurrence_array[arr_index] += 1
#
#     max_occurrence = 0
#     max_alphabet_index = 0
#     for index in range(len(alphabet_occurrence_array)):
#         alphabet_occurrence = alphabet_occurrence_array[index]
#         if alphabet_occurrence > max_occurrence:
#             max_occurrence = alphabet_occurrence
#             max_alphabet_index = index
#
#     return chr(max_alphabet_index + ord('a'))


