class Solution:
    def isValid(self, s: str) -> bool:

        my_stack = []
        pairs = {')':'(', ']':'[', '}':'{'}

        for ch in s:
            if ch in pairs: #Only checks the keys not the values
                if not my_stack or my_stack[-1] != pairs[ch]:
                    return False 
                my_stack.pop()
            else:
                my_stack.append(ch)
        return not my_stack #The stack should be empty at the end if the string is valid.

