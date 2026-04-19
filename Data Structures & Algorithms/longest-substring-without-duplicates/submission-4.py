class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_chars = set()
        l = 0
        max_length = 0

        for r in range(len(s)):
            while s[r] in current_chars: 
                current_chars.remove(s[l])
                l += 1
            current_chars.add(s[r])
            max_length = max(max_length, r - l + 1)
        return max_length