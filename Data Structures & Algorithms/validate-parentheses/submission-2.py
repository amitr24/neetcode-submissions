class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesis = {'(': ')', '{': '}', '[' : ']'}
        for char in s:
            if char == '(' or char == '[' or char =='{':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                popped_paren = stack.pop()
                if parenthesis[popped_paren] != char:   
                    return False
        return len(stack) == 0
                