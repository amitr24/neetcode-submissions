from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        
        frequency_list = {num : nums.count(num) for num in nums}  

        descending_frequency = dict(sorted(frequency_list.items(), key=lambda item : item[1], reverse=True))

        return list(descending_frequency.keys())[:k]'''

        frequency_list = {i: [] for i in range(len(nums)+1)}

        for num in set(nums):
            frequency_list[nums.count(num)].append(num)
        top_k = []
        for i in range(len(frequency_list)-1, -1, -1):
            if len(top_k) < k:
                top_k.extend(list(frequency_list.values())[i][:k - len(top_k)])

        return top_k