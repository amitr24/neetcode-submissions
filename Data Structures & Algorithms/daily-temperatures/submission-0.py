class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0 for _ in range(len(temperatures))]
        stack = []
        
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                t = stack.pop()
                out[t] = i - t
            stack.append(i)

        return out