class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        letters = {}

        for l in magazine:
            if l in letters:    
                letters [l] += 1 
            else:
                letters [l] = 1

        for c in ransomNote:
            if c not in letters: return False
            if letters[c] == 1: del letters[c] 
            else: letters[c] -= 1
            
        return True