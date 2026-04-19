class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        subset = []

        def back_track(i, target):
            if target == 0:
                results.append(subset.copy())
                return
            if i >= len(nums) or target < 0:
                return

            # include nums[i]
            subset.append(nums[i])
            back_track(i, target - nums[i])  # allow reuse of same element
            subset.pop()

            # skip nums[i]
            back_track(i + 1, target)

        back_track(0, target)
        return results
