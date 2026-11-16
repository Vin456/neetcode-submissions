class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hashmap = {}
        t_hashmap = {}

        if len(s) != len(t):
            return False
        
        if len(s) == 1 and len(t) == 1 and s == t:
            return True

        for i in range(len(s)):
            s_hashmap[s[i]] = s_hashmap.get(s[i],0) + 1
            t_hashmap[t[i]] = t_hashmap.get(t[i],0) + 1

        for c in s_hashmap:
            if s_hashmap[c] != t_hashmap.get(c,0):
                return False
        return True