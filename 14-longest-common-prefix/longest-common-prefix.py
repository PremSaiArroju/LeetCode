class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        # Start with the first string in the list as the initial prefix
        prefix = strs[0]

        # Compare the prefix with each string in the list
        for string in strs[1:]:
            while string[:len(prefix)] != prefix:
                # Shorten the prefix until it matches
                prefix = prefix[:-1]
                # If the prefix becomes empty, there's no common prefix
                if not prefix:
                    return ""

        return prefix