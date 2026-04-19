class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        differences = [target - x for x in nums]
        for i in range(len(nums)):
            j = differences.index(nums[i]) if nums[i] in differences else -1
            if j != -1 and i != j:
                return sorted([i, j])