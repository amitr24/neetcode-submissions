class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
            
        frequency_list = {}
        for x in nums:
            if x in frequency_list.keys(): 
                return True
            frequency_list[x] = 1

        return False