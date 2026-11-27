class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency={}
        res=[]
        for i in nums:
            if i not in frequency:
                frequency[i] = 1
            else:
                frequency[i] = frequency[i]+1
        
        sorted_freq = dict(sorted(frequency.items(), key= lambda item: item[1], reverse=True))

        return list(sorted_freq)[:k]

