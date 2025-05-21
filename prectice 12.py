"""def factorial():
    result = 1
    for i in range(1, 6):
        result *= i
    return result

print(factorial())"""

'''def factorial(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(4))'''

def factorial(n):
    
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


n_str = input("Enter a non-negative integer: ")
n = int(n_str)  
if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(n)
    print(f"The factorial of {n} is {result}")

