class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = Counter(nums)

        for i in hashmap:
            if hashmap[i] == 1:
                return i