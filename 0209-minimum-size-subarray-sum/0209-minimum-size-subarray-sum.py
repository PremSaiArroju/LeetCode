class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #Array and Sliding Window
        left = 0
        total = 0
        min_length = float('inf')
        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                min_length = min(min_length, right-left+1)
                total -= nums[left]
                left += 1

        if min_length != float('inf'):
            return min_length
        else:
            return 0