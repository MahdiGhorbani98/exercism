from math import isqrt

def classify(number):
    if not isinstance(number, int) or number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    total = 0
    for i in range(1, isqrt(number) + 1):
        if number % i == 0:
            if i != number:          # خود عدد رو حساب نکن (برای i=1 وقتی number=1)
                total += i
            paired = number // i
            if paired != i and paired != number:
                total += paired
    
    if total > number:
        return "abundant"
    elif total == number:
        return "perfect"
    return "deficient"