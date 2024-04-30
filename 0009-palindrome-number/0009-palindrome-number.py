class Solution:
    def isPalindrome(self, x: int) -> bool:
        k = ""
        x = str(x)
        for i in x:
            k = i + k

        if x == k:
            return True
        return False