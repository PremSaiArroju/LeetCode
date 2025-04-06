class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)  # Remove duplicates and allow O(1) lookups
        longest = 0          # To track the longest sequence found

        for num in num_set:
            # Only start counting if this is the start of a sequence
            if num - 1 not in num_set:
                current = num
                length = 1

                # Keep checking next numbers in the sequence
                while current + 1 in num_set:
                    current += 1
                    length += 1

                # Update longest if this sequence is the longest so far
                longest = max(longest, length)

        return longest