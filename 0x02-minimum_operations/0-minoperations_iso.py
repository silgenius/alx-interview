def minOperations(n: int) -> int:
    """a method that calculates the fewest number of operations needed
    to result in exactly n H characters in the file.

    Args:
        n (int): Number of H's

    Returns:
        int: Number of operations
    """
    if n <= 1:
        return 0
    
    result = 1
    nop = 0
    copy = 1
    while True:
        if result == n: # n is const
            return nop
        if copy + result > n:  # Try to Copy all and paste
            result += copy # Paste current buffer instead
            nop += 1
        else:
            result += copy # Copy all and paste
            nop += 2 # Copy all and Paste is 2 operations
            copy = result