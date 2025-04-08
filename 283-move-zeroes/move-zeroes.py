class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNonZeroFoundAt = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                if i != lastNonZeroFoundAt:
                    nums[i], nums[lastNonZeroFoundAt] = nums[lastNonZeroFoundAt], nums[i]
                lastNonZeroFoundAt += 1