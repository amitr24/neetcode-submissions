class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums) <= 1):
            return len(nums)
        starts = []
        for i in range(len(nums)):
            if(nums[i]-1 not in nums):
                starts.append(i)
        print(starts)
        maxLength = 0
        for i in starts: 
            lengthOfSequence = 1
            print(i)
            index = nums.index(nums[i]+lengthOfSequence) if nums[i]+lengthOfSequence in nums else -1
            
            while(index != -1):
                lengthOfSequence+=1
                index = nums.index(nums[i]+lengthOfSequence) if nums[i]+lengthOfSequence in nums else -1
            maxLength = max(lengthOfSequence, maxLength)

        return maxLength