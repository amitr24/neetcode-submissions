class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_forward = [1] * len(nums)
        product_backward = [1] * len(nums)
        product_except_self = [1] * len(nums)
        n = len(nums)
        for i in range(1, n):
            product_forward[i] = product_forward[i-1] * nums[i-1]

        for i in range(n-2, -1, -1):
            product_backward[i] = product_backward[i+1] * nums[i+1]

        for i in range(n):
            product_except_self[i] = product_forward[i] * product_backward[i]

        return product_except_self
