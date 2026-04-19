class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        
        for num in nums:
            frequency[num] += 1
        
        return [num for num, count in sorted(frequency.items(), key=lambda x: x[1], reverse=True)[:k]]
