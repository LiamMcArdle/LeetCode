class Solution:
    def climbStairs(self, n: int) -> int:
        
        #work backwards from n
        previous, current = 1, 1
        
        for i in range(n-1):
            temp = current
            current = current + previous
            previous = temp
            
        return current