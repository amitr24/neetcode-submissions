class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        frequency_list = {}
        s_char = list(s)
        t_char = list(t)

        for i in range(len(s_char)):
            char_s = s_char[i]
            char_t = t_char[i]
            if(s_char[i] not in frequency_list.keys()):
                frequency_list[char_s] = 0
            frequency_list[char_s] += 1
            if(char_t not in frequency_list.keys()):
                frequency_list[char_t] = 0
            frequency_list[char_t] -= 1
        print(frequency_list)
        unique_characters = [key for key, value in frequency_list.items() if value != 0]
        return len(unique_characters) == 0