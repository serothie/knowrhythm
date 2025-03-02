input = 20

# def find_prime_list_under_number(number):
#     primes = []
#     for d in range(2, number + 1):
#         for n in range(2, d):
#             if d % n == 0:
#                 break
#         else:
#             primes.append(d)
#     return primes

# for else : for문의 모든 루프가 정상적으로 전부 완료되면 else문이 실행
# 어느 배열에 무언가 있는지 업는지 판단하기 좋음
# break가 실행되면 else문이 실행되지 않는다.

# def find_prime_list_under_number(number):
#     primes = []
#     for d in range(2, number + 1):
#         # 불필요하게 모든 나머지 숫자를 찾을 필요는 없다
#         for n in primes:
#             if d % n == 0:
#                 break
#         else:
#             primes.append(d)
#     return primes

# 자연수 N이 소수이기 위한 필요충분조건: N 제곱근보다 크지 않은 어떤 소수로도 나누어 떨어지지 않는다.
def find_prime_list_under_number(number):
    primes = []
    for d in range(2, number + 1):
        # 필요충분조건 활용한다
        for n in primes:
            if n ** 2 <= d and d % n == 0:
                break
        else:
            primes.append(d)
    return primes


result = find_prime_list_under_number(input)
print(result)