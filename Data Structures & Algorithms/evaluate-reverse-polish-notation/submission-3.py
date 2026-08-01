class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            try:
                if isinstance(int(i), int):
                    stack.append(int(i))
            except:
                a, b = stack.pop(), stack.pop()
                if i == "+":
                    stack.append(a+b)
                elif i == "-":
                    stack.append(b-a)
                elif i == "*":
                    stack.append(a*b)
                else:
                    stack.append(int(b/a))
        return stack[0]


        