class Solution:
    def findMin(self, nums: List[int]) -> int:
        cutpoint = 0
        low = 0
        high = len(nums) - 1
        while (low < high):
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        cutpoint = low
        return nums[high]



# 3, 4, 5, 6, 1, 2
# low = 3, 4, mid = 5, 6, 1, high = 2

# 3, 4, 5, low = 6, mid = 1, high = 2
# 3, 4, 5, low = 6, high = 1, 2