class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        parens = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }
        
        for i in s:
            if i in parens:
                stack.append(i)
            elif not stack or parens[stack.pop()] != i:
                return False        
        

        return not stack
