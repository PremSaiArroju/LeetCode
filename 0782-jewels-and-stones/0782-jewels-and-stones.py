class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        jewels = set([j for j in jewels]) 
        #This creates set to filter unique values in jewels to increase runtime to O(N+M)
        
        for s in stones:
            if s in jewels:
                count += 1
        return count
        
        """
        #This takes runtime of O(N*M) for large sets
        count = 0
        for s in stones:
            if s in jewels:
                count += 1
        
        return count
        """