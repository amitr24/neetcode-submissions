class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        consecutive_sequence = set(nums)
        longest = 0
        for i in consecutive_sequence:
            if i-1 not in consecutive_sequence: 
                length = 1
                while (i+length) in consecutive_sequence: 
                    length += 1
                longest = max(length, longest)

        return longest