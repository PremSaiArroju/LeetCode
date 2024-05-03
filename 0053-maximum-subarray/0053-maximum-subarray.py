class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_sum = 0
        max_sum = float('-inf')
        n = len(nums)

        for i in range(n):
            current_sum = current_sum + nums[i]
            max_sum = max(max_sum, current_sum)
            if current_sum < 0:
                current_sum = 0
        
        return max_sum
        