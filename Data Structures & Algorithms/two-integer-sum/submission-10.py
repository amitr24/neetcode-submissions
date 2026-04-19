class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference = {}
        # Iterate through
        for i, num in enumerate(nums):
            complement = target-num

            if complement in difference:
                return [difference[complement], i]
            difference[num] = i
        return []