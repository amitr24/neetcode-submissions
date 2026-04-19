class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                index = ord(c)-ord('a')
                count[index] += 1
            count = tuple (count)
            if(count in anagrams):
                anagrams[count].append(s)
            else:
                anagrams[count] = [s]
        return anagrams.values()