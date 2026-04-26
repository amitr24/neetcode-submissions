class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "#" + s
        return encoded_str
    def decode(self, s: str) -> List[str]:
        curr_s = ""
        length = 0
        decoded_strings = []
        i = 0
        while(i < len(s)):
            

            # keep track of string before you hit a #
            # Then get the subsequesent string of that size
            char = s[i]
            if char == '#':
                print(s[i+1:i+1+int(curr_s)])
                decoded_strings.append(s[i+1:i+1+int(curr_s)])
                i = i+1+int(curr_s)
                curr_s = ""
                
            else:
                curr_s = curr_s + char
                i+=1

        return decoded_strings