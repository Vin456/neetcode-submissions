class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency={}
        res=[]
        for i in nums:
            if i not in frequency:
                frequency[i] = 1
            else:
                frequency[i]+=1
        
        sorted_freq = dict(sorted(frequency.items(), key= lambda item: item[1], reverse=True))

        keys = list(sorted_freq)   # keys in sorted order, most frequent first

        for j in range(k):
            res.append(keys[j])
        return res

