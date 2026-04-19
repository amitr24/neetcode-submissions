class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x in tokens:
            if(x=='+'):
                stack.append(stack.pop()+stack.pop())
            elif(x=='-'):
                stack.append(-stack.pop()+stack.pop())
            elif(x=='/'):
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b)/a))
            elif(x=='*'):
                stack.append(stack.pop()*stack.pop())
            else:
                stack.append(int(x))
        return stack.pop()