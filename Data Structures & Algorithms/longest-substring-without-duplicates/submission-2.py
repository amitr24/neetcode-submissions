class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        listOfChar = []
        maxLength = 0
        for i in range(0, len(s)):
            if(s[i] not in listOfChar):
                listOfChar.append(s[i])
            else:
                if(maxLength<len(listOfChar)):
                    maxLength = len(listOfChar)
                listOfChar = listOfChar[listOfChar.index(s[i])+1:]
                listOfChar.append(s[i])
                print(listOfChar)
        if(maxLength<len(listOfChar)):
            maxLength = len(listOfChar)
        return maxLength