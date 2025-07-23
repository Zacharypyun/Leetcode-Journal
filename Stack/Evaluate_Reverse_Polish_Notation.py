class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            try:
                stack.append(int(i)) 
            except ValueError:
                b = stack.pop()
                a = stack.pop()
                if i == "+":
                    stack.append(a + b)
                elif i == "-":
                    stack.append(a - b)
                elif i == "*":
                    stack.append(a * b)
                else:  # division
                    stack.append(int(a / b)) 
        return stack[0]
