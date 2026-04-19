class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        starts = []
        threeSum =[]
        for i in range(0, len(nums)-2):
            if(nums[i] in starts):
                continue
            left = i+1
            right = len(nums)-1
            currentSum = nums[i] + nums[left] + nums[right]
            starts.append(nums[i])
            while(left<right):
                if(nums[i] == -1):
                    print(f"{nums[left]} and {nums[right]}")
                if(currentSum < 0):
                    left += 1
                elif(currentSum == 0):
                    threeSum.append([nums[i], nums[left], nums[right]])
                    j = nums[left]
                    while(left < len(nums) - 1 and nums[left] == j):
                        print("A")
                        left += 1
                else:
                    right -= 1
                currentSum = nums[i] + nums[left] + nums[right]

        return threeSum