class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operators = ['+','-','/','*']
        myStack = []

        for token in tokens:
            if token not in operators:
                myStack.append(int(token))
            if token in operators:
                right = myStack.pop()
                left = myStack.pop()
                if token == '+': 
                    myStack.append(int(left + right))
                if token == '-': 
                    myStack.append(int(left - right))
                if token == '/': 
                    myStack.append(int(left / right))
                if token == '*': 
                    myStack.append(int(left * right))

        return myStack.pop()