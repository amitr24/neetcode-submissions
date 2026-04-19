class Solution:

    def encode(self, strs: List[str]) -> str:
        delimiter = "|*,"
        encoded_str = ""
        for string in strs: 
            encoded_str = encoded_str + delimiter + string

        return encoded_str
    def decode(self, s: str) -> List[str]:
        delimiter = "|*,"
        strs = s.split(delimiter)

        return strs[1:]

