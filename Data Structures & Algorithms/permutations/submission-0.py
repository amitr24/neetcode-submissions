class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        boolean_list = [False] * len(nums)
        set_chosen = set([])
        permutation = []
        def back_track(set_chosen, permutation):
            if len(set_chosen) == len(nums):
                results.append(list(permutation.copy()))
            for i in nums:
                if i not in set_chosen:
                    set_chosen.add(i)
                    permutation.append(i)
                    back_track(set_chosen, permutation)
                    permutation.pop()
                    set_chosen.remove(i)
        back_track(set_chosen, permutation)
        return results