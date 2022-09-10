class Solution:
    def isValid(self, s: str) -> bool:
        stack = []                              #stack in form of list to push delimiters to
        pairs = {'(':')', '[':']', '{':'}'}     #dictionary of matching delimiters
        for i in s:                             #for each delimiter
            if i in '([{':                      #if opening push
                stack.append(i)                 
            else:                               #else check if stack empty or delimiter doesn't match top
                if len(stack) == 0 or i != pairs[stack.pop()]:
                    return False                #if so return false
        return len(stack) == 0                  #after all characters processed return bool of stack empty