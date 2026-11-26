class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in strs:
            freq=[0] * 26
            for j in i:
                freq[ord(j)-ord('a')]+=1
            freq_tup = tuple(freq)
            if freq_tup in res:
                res[freq_tup].append(i)
            else:
                res[freq_tup] = [i]
        return list(res.values())