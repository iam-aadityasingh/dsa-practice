def isPowerOfThree(self, n: int) -> bool:
        ans = 3

        if n == 1:
            return True

        while ans < n:
            ans *= 3
            
        if ans == n:
            return True
        else:
            return False