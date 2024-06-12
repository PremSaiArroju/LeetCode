class Solution:
    def isValid(self, word: str) -> bool:
        vowels = 'aeiou'
        consonants = 'qwrtyplkjhgfdszxcvbnm'
        vowels += vowels.upper()
        consonants += consonants.upper()
        allowed = vowels + consonants + '0123456789'

        if len(word) < 3: return False
        has_vowel = False
        has_consonant = False
        for c in word:
            if c in vowels: has_vowel = True
            if c in consonants: has_consonant = True
            if c not in allowed: return False

        return has_vowel and has_consonant