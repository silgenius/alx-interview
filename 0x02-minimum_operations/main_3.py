def minOperations(n):
    if n <= 1:
        return 0
    
    operations = 0
    factor = 2
    
    while factor * factor <= n:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    
    # If n is still greater than 1, it must be a prime number
    if n > 1:
        operations += n
    
    return operations
