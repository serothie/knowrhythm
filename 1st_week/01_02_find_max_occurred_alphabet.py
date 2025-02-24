from operator import indexOf


def find_max_occurred_alphabet(string):
    # 이 부분을 채워보세요!
    alphabet_occurrence_array = [0] * 26
    for char in string:
        if char != ' ':
            alphabet_occurrence_array[ord(char) - 97] += 1
    return chr(alphabet_occurrence_array.index(max(alphabet_occurrence_array)) + 97)


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))