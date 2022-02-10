# Recursion - Factorial

def findFactorial(num):
    if num == 1 or num == 2:
        return(num)
    else:
        return num * findFactorial(num-1)

print(findFactorial(5))


# Fibonacci series
# 0,1,1,2,3,5,8,13,21,34,55

def fibonacci(N):
    if N == 1:
        return(0)
    elif N == 2:
        return(1)
    else:
        return fibonacci(N-1) + fibonacci(N-2)

print(fibonacci(5))

# fibonacci(5) = fibonacci(4) + fibonacci(3)
#             = fibonacci(3) + fibonacci(2) + fibonacci(2) + fibonacci(1)
#             = fibonacci(2) + fibonacci(1) + 1 + 1 + 0
#             = 1 + 0 + 2
#             = 3
