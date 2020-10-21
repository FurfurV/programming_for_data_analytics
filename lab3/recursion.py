# Created by Viktoria 
# (▰˘◡˘▰)
# 21/10/2020
# Student number: R00180598



def fibonacci_recursion(n):
    if(n <=1):
        return 0
    elif(n <= 3):
        return 1
    else:
        return fibonacci_recursion(n-1)+fibonacci_recursion(n-2)

print(fibonacci_recursion(5))
print(fibonacci_recursion(13))

def prime_recursion(n,i):
    if (n <= 2):
        print(n)
        return True

    if (n % i == 0):
        return False

    if(i * i > n):
        return True

    return prime_recursion(n, i + 1)

print(prime_recursion(27,2))


