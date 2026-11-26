class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq_map = {}
        n = len(nums)
        for i in range(n):
            diff = target - nums[i]
            if diff in freq_map and i != freq_map[diff]:
                return [freq_map[diff], i]
            else:
                freq_map[nums[i]] = i
        