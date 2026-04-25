from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a Frequency List
        frequency_list = [0 for x in range(26)] # Frequency of every letter
        grouping = defaultdict(list)
        for i in range(len(strs)):
            for s in set(strs[i]):
                s = s.lower()
                frequency_list[ord(s) - ord('a')] = strs[i].count(s)
            grouping[tuple(frequency_list)].append(strs[i])
            frequency_list = [0 for x in range(26)]

        return list(grouping.values())