class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}                                   #declare hash table
        for i in range(len(nums)):                  #iterate over all values in nums
            num = nums[i]                           #declare an int to save time, sacrifice memory 
            if target - num in hash:                #if the complement of the number is in the hash table, we return
                return (hash[target - num], i)      
            hash[num] = i                           
        return None