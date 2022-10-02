class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ''
        
        #Convert to list
        a = list(a)
        b = list(b)
        
        #while we have one of the following true...
        while a or b or carry:
            #if either a or b are 1 pop from list and add them to the carry as int
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            
            #add the string of the remainder of carry
            result += str(carry % 2)
            #floor division (i.e. will only be 1 if carry is 2 beforehand)
            carry //= 2
        return result[::-1] #return the reverse of result