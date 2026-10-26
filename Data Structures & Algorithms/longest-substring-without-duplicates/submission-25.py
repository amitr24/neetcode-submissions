class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring_alpha = set()
        max_substring_length = 0
        i = 0

        for j in range(len(s)):
            while s[j] in substring_alpha:
                substring_alpha.remove(s[i])
                i += 1

            substring_alpha.add(s[j])
            max_substring_length = max(
                max_substring_length, j - i + 1
            )

        return max_substring_length