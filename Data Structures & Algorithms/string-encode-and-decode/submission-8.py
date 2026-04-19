class Solution:

    def encode(self, strs: List[str]) -> str:
        if(strs!=[]):
            s = strs[0]
            for string in strs[1:]:
                s = s + "|" + string
            return s
        return None
    def decode(self, s: str) -> List[str]:
        if(s is None):
            return []
        splitString = s.split("|")
        return splitString