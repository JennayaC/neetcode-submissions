class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        myStack = []

        for token in tokens:
            if token == '+':
                right = myStack.pop()
                left = myStack.pop()
                result = right + left
                myStack.append(int(result))
            elif token == '-':
                right = myStack.pop()
                left = myStack.pop()
                result = left - right
                myStack.append(int(result))
            elif token == '*':
                right = myStack.pop()
                left = myStack.pop()
                result = left * right
                myStack.append(int(result))
            elif token == '/':
                right = myStack.pop()
                left = myStack.pop()
                result = left / right
                myStack.append(int(result))
            else:
                num = int(token)
                myStack.append(num)
        return myStack.pop()
