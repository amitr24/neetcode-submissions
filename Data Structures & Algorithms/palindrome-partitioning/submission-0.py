class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def back_track(start, subset):
            # base case: reached the end of the string
            if start == len(s):
                result.append(subset.copy())
                return

            # try all possible end positions for the next substring
            for end in range(start, len(s)):
                substring = s[start:end+1]
                if substring == substring[::-1]:  # palindrome check
                    subset.append(substring)
                    back_track(end + 1, subset)
                    subset.pop()  # backtrack

        back_track(0, [])
        return result
