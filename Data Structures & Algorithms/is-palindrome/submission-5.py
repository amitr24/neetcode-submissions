class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            # If the left character isn't alphanumeric, skip it
            while left < right and not s[left].isalnum():
                left += 1
                
            # If the right character isn't alphanumeric, skip it
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare the valid characters (lowercased)
            if s[left].lower() != s[right].lower():
                return False
            
            # Move both pointers inward
            left += 1
            right -= 1
            
        return True