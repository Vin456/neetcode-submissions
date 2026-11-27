class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency={}
        res=[[] for i in range(len(nums)+1)]
        for i in nums:
            if i not in frequency:
                frequency[i] = 1
            else:
                frequency[i]+=1
        
        for key,v in frequency.items():
            res[v].append(key)

        sol = []
        for j in range(len(res)-1,0,-1):
            for n in res[j]:
                sol.append(n)
                if len(sol) == k:
                    return sol