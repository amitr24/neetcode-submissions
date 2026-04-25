from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a Frequency List

        grouping = defaultdict(list)
        for i in range(len(strs)):
            s = tuple(sorted(strs[i])) 
            grouping[s].append(strs[i])

        return list(grouping.values())