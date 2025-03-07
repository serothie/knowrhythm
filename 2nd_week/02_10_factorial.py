# 무언가 반복되는 것 같다 싶으면 한다

def factorial(n):
    if n == 1 :
        return 1

    return n * factorial(n - 1)


print(factorial(5))