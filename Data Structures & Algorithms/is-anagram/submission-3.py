class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Maybe try to find frequency of all letters
        # Whats the best way of doing this? 
        frequency_list_s = {x:  s.count(x) for x in set(s)}

        frequency_list_t = {x: t.count(x) for x in set(t)}
        print(frequency_list_s)
        print(frequency_list_t)
        return frequency_list_s == frequency_list_t