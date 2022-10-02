class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max, max_until_now = 0, -inf
        for num in nums:
            current_max = max(num, current_max + num)
            max_until_now = max(current_max, max_until_now)
        return max_until_now