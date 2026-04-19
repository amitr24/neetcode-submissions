class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Frequency list? 
        # Keep track of max? 
        
        frequencies = defaultdict(int)

        for i in nums:
            frequencies[i] += 1
        buckets = [set() for _ in range(len(nums) + 1)]        
        for num, frequency in frequencies.items():
            buckets[frequency].add(num)
        result = []
        for i in range(len(nums), 0, -1):
            if len(result) < k:
                result.extend(buckets[i])
        return result