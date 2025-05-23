class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s_t = {}
        map_t_s = {}

        for i in range(len(s)):
            if s[i] not in map_s_t:
                map_s_t[s[i]] = i

            if t[i] not in map_t_s:
                map_t_s[t[i]] = i
            
            if map_s_t[s[i]] != map_t_s[t[i]]:
                return False

        return True