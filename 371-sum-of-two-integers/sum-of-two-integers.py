class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF  # To handle 32-bit overflow
        MAX_INT = 0x7FFFFFFF

        while b != 0:
            carry = (a & b) & MASK      # Calculate carry
            a = (a ^ b) & MASK          # Sum without carry
            b = (carry << 1) & MASK     # Prepare new carry
        
        # If a is greater than MAX_INT, it means it's a negative number
        return a if a <= MAX_INT else ~(a ^ MASK)