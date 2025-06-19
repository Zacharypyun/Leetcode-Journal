class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        stack = []
        check = {')': '(', '}': '{', ']': '['}
        
        for i in s:
            if i in check.values():
                stack.append(i)
            elif i in check:
                if not stack or stack[-1] != check[i]:
                    return False
                stack.pop()
            else:
                return False 
        if len(stack) != 0:
            return False
        return True