class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_except_self_array = [1] * len(nums)
        # Forward pass: 
            # Let x be the curr product of numbers from 0 to i-1 for i
            # Multiply i by x
            # Update x by multiplying by i
        x = 1
        for i in range(len(nums)):
            product_except_self_array[i] = x
            x *= nums[i]
        # Backward pass:
            # Let y be the curr product of numbers from len(nums) -1 to i+1
            # Multiply i by y
            # Update y by multiply by i
        y = 1
        for i in range(len(nums)-1, -1, -1):
            product_except_self_array[i] = product_except_self_array[i] * y
            y *= nums[i]
        # Done
        return product_except_self_array