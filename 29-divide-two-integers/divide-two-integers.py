class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants to handle overflow
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Handle edge case for overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)

        # Use absolute values for calculations
        dividend, divisor = abs(dividend), abs(divisor)

        # Initialize quotient
        quotient = 0

        # Perform division using bit shifting
        while dividend >= divisor:
            current_divisor, num_shifts = divisor, 0
            while dividend >= (current_divisor << 1):
                current_divisor <<= 1
                num_shifts += 1
            dividend -= current_divisor
            quotient += 1 << num_shifts

        # Apply sign
        if negative:
            quotient = -quotient

        # Clamp the result to the 32-bit signed integer range
        return max(INT_MIN, min(INT_MAX, quotient))