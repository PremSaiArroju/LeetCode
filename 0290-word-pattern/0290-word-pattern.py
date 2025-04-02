class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        # Check if lengths match
        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for c, w in zip(pattern, words):
            # Check both mappings
            if c in char_to_word and char_to_word[c] != w:
                return False
            if w in word_to_char and word_to_char[w] != c:
                return False

            # Create mapping if not yet mapped
            char_to_word[c] = w
            word_to_char[w] = c

        return True

