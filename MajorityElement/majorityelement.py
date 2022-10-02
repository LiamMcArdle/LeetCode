class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Get dict with number of occurrences for each number
        #Find label with max number of occurrences and return
        vals = Counter(nums)
        max_label = max(vals, key = vals.get)
        return max_label