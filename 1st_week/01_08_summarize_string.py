def summarize_string(input_str):
    # 이 부분을 채워보세요!
    result = ''
    alphabets = [0] * 26
    for char in input_str:
        alphabets[ord(char) - ord('a')] += 1
    for i in range(len(alphabets)):
        occurrence = alphabets[i]
        if occurrence:
            result += f'/{chr(i + ord('a'))}{occurrence}'
    return result[1:]

input_str = "acccdeee"

# def summarize_string(target_string):
#     # 이 부분을 채워보세요!
#     n = len(target_string)
#     count = 0
#     result_str = ''
#
#     for i in range(n - 1):
#         if target_string[i] == target_string[i + 1]:
#             count += 1
#         else:
#             result_str += target_string[i] + str(count + 1) + '/'
#             count = 0
#
#     result_str += target_string[n - 1] + str(count + 1)
#
#     return result_str

# 소문자 알파벳순이라는 조건이 있었다

print(summarize_string(input_str))