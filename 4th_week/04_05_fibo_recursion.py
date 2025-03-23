input = 100


def fibo_recursion(n):
    if n == 1 or n == 2:
        return 1
    return fibo_recursion(n - 1) + fibo_recursion(n - 2)

# 이미 했던 작업을 계속 다시 하게 됩니다.
# 이미 시켰던 똑같은 작업을 다른 곳에서 다시 새롭게 하고 있는겁니다.
# 이런 "삽질" 을 계속 시키지 않으려면, 이미 했던 일을 기록하고 있어야 합니다.
# 그 방법에 대해서 동적 계획법에서 배워 봅시다.

print(fibo_recursion(input))  # 6765