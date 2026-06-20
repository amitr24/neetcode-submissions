from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Have a running set of alphabets where we have two points left and right
        # They dictate which substring we are looking at
        if not s:
            return 0
        l = 0
        r = 0

        recent_index_lookup = defaultdict(int)
        max_len = 1

        recent_index_lookup[s[l]] = l

        while (r < len(s) - 1):
            r += 1
            if(s[r] in recent_index_lookup.keys()):
                l = max(l, recent_index_lookup[s[r]] + 1)

            recent_index_lookup[s[r]] = r

            max_len = max(max_len, r - l + 1)
            print(s[l:r+1], r)

        return max_len