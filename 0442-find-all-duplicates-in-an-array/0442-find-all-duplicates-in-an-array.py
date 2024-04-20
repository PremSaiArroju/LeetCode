class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        #create an empty array
        for num in nums:
        # If the number at index |num| - 1 is negative, it has been visited before
            if nums[abs(num) - 1] < 0:
             duplicates.append(abs(num))
            else:
            # Mark the number at index |num| - 1 as visited by making it negative
                nums[abs(num) - 1] *= -1
        return duplicates