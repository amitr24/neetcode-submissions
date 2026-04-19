class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = [char for char in s if isAlphaNumeric(char)]
        left = 0
        right = len(s) - 1
        while (left < right):
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True
def isAlphaNumeric(s:str):
    return 'a' <= s <= 'z' or '0' <= s<= '9'
