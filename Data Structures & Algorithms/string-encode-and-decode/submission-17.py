class Solution:

    def encode(self, strs: List[str]) -> str:
        if(strs!=[]):
            totalStr = ""
            for s in strs:
                totalStr += str(len(s)) + '#' + s
            print(totalStr)
            return totalStr
            
        return ""
    def decode(self, s: str) -> List[str]:
        if(s==""):
            return []
        strList = []
        i = 0
        while(i<len(s)):
            print(s[i])
            j = i
            while(s[j]!='#'):
                j+=1
            length = int(s[i:j])
            strList.append(s[j+1 : j+1+length])
            i = j+1+length
        return strList