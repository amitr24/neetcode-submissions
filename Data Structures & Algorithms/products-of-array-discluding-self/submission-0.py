import numpy
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        outputArray = numpy.ones(len(nums))
        for i in range(0, len(nums)):
            temp = outputArray[i]
            outputArray = nums[i]*outputArray
            outputArray[i] = temp
        return outputArray.astype(int)