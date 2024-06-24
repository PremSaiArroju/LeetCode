class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        res = 0
        n = 2 * n
        for k in range(1, int(sqrt(n))+1):
            if n % k == 0 and n // k > k and (n // k - (k-1)) % 2 == 0:
                res += 1
        
        return res
        