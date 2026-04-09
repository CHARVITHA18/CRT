def sum_of_digits(n: int) -> int:
    total = 0
    n = abs(n)
    
    while n > 0:
        digit = n % 10
        total += digit
        n //= 10
        
    return total