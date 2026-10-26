class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) == 0:
            return []
        intermediate_sum = {target - nums[i] : i for i in range(len(nums))}
        for j in range(len(nums)):
            if nums[j] in intermediate_sum.keys() and j != intermediate_sum[nums[j]]:
                return sorted([j, intermediate_sum[nums[j]]])

        return []