"""def is_prime (num):
    if num <= 1:
        return True
    for i in range (2, num):
        if num % i == 0:
            return False
    return True
print(is_prime(1))"""

def second_largest(number):
    if len(number) < 2:
        return None
    largest = second = float('-inf')
    for num in number:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    return second if second != float('-inf') else None

print(second_largest([3, 5, 7, 2, 8, 1]))