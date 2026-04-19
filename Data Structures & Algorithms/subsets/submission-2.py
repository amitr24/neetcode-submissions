class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        possible_nums = []
        subset = []
        def back_track(i):
            
            if i >= len(nums):
                possible_nums.append(subset.copy())
                return

            subset.append(nums[i])
            back_track(i+1)
            subset.pop()
            back_track(i+1)

        back_track(0)

        return possible_nums