class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        if not nums:
            return result

        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                # Range ends here
                if start == nums[i-1]:
                    result.append(str(start))
                else:
                    result.append(f"{start}->{nums[i-1]}")
                start = nums[i]  # Start new range

        # Add the last range after loop
        if start == nums[-1]:
            result.append(str(start))
        else:
            result.append(f"{start}->{nums[-1]}")

        return result