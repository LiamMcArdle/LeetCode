class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        vals = Counter(nums)
        for (key, value) in vals.items(): 
            if value > 1: 
                return True
        return False