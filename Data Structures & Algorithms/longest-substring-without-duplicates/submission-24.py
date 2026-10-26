class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring_alpha = set()
        max_substring_length = 0
        i = 0
        j = 0

        if len(s) == 0:
            return 0

        while (j < len(s)):
            substring_alpha.add(s[j])
            j += 1
            while j < len(s) and s[j] not in substring_alpha :
                substring_alpha.add(s[j])
                j += 1
            
            while j < len(s) and s[j] in substring_alpha:
                max_substring_length = max(j-i, max_substring_length)
                substring_alpha.remove(s[i])
                i += 1
        max_substring_length = max(j-i, max_substring_length)
        return max_substring_length