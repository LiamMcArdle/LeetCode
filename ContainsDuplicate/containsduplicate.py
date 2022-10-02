class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        vals = Counter(nums)
        max_val = max(vals.values())
        return max_val > 1