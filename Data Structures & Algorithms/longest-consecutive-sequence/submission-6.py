class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # No sorting due to time constraints
        if len(nums) == 0:
            return 0
        set_nums = set(nums)
        curr_len = 1
        max_len = 1
        for num in set_nums:
            if num-1 not in set_nums:
                curr_len = 1
                while num + curr_len in set_nums:
                    curr_len += 1
                max_len = max(curr_len, max_len)
        return max_len