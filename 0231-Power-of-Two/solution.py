def isPowerOfTwo(n: int) -> bool:
    ans = 1

    if n <= 0:
        return False

    if n == 1:
        return True

    while ans < n:
        ans *= 2
    return ans == n

            
        
