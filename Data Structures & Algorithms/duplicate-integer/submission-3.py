class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_elements = set(nums)

        return len(set_elements) != len(nums)