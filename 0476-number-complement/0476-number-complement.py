class Solution:
    def findComplement(self, num: int) -> int:
        bit_length = num.bit_length()  # Number of bits in binary representation
        mask = (1 << bit_length) - 1   # Bitmask with all bits set
        return num ^ mask              # XOR to flip bits