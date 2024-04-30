class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s = {}
        for i, value in enumerate(nums): #1
            remaining = target - nums[i] #2
           
            if remaining in s: #3
                return [i, s[remaining]]  #4
            else:
                s[value] = i  #5