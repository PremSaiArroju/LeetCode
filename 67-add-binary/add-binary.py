class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0 or carry:
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0

            # Binary addition
            total = digit_a + digit_b + carry
            carry = total // 2  # Update the carry
            result.append(str(total % 2))  # Add the binary result (0 or 1)

            i -= 1
            j -= 1

        # Reverse the result and join to form the binary string
        return ''.join(reversed(result))