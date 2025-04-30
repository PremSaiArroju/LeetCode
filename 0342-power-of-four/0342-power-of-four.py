class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        
        # Check if n is a power of two (only one bit set)
        if (n & (n - 1)) != 0:
            return False
        
        # Check if (n - 1) is divisible by 3 (only true for powers of 4)
        if (n - 1) % 3 != 0:
            return False

        return True