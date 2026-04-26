class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_list = {num : nums.count(num) for num in nums}  

        descending_frequency = dict(sorted(frequency_list.items(), key=lambda item : item[1], reverse=True))

        return list(descending_frequency.keys())[:k]