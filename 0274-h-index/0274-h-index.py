class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Sort the citations in descending order
        citations.sort(reverse=True)
        
        h_index = 0
        # Iterate through the sorted array
        for i, c in enumerate(citations):
            # Check if the current paper satisfies the h-index condition
            if i + 1 <= c:
                h_index = i + 1
            else:
                break        
        return h_index