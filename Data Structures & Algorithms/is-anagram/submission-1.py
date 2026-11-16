class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hashmap = {}
        t_hashmap = {}

        if len(s) != len(t):
            return False
        
        if len(s) == 1 and len(t) == 1 and s == t:
            return True

        for s_char in s:
            if s_char in s_hashmap:
                s_hashmap[s_char] += 1
            else:
                s_hashmap[s_char] = 1
        for t_char in t:
            if t_char in t_hashmap:
                t_hashmap[t_char] += 1
            else:
                t_hashmap[t_char] = 1

        if s_hashmap == t_hashmap:
            return True
        else:
            return False