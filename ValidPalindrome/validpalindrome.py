class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = "".join(c for c in s if c.isalnum()).lower()
        return s_new == s_new[::-1]
