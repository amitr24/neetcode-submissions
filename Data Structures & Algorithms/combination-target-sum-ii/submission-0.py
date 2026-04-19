class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = [] 

        subset = []

        def back_track(i, target_minus_sum):

            if target_minus_sum == 0:
                result.append(subset.copy())
                return
            if i >= len(candidates):
                return
            subset.append(candidates[i])
            back_track(i+1, target_minus_sum-candidates[i])
            subset.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1    
            back_track(i+1, target_minus_sum)

        
        back_track(0, target)

        return result
