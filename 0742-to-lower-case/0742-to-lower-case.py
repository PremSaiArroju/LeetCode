class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = ""
        for c in s:
            n = ord(c)
            if n > 64 and n < 91:
                ans += chr(n+32)
            else:
                ans += c
        return ans