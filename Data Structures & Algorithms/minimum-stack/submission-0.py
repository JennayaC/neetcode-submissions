class MinStack:

    def __init__(self):
        self.stack = []
        self.Minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.Minstack or self.Minstack[-1] >= val:
            self.Minstack.append(val)
        


    def pop(self) -> None:
        val = self.stack.pop()

        if val == self.Minstack[-1]:
            self.Minstack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.Minstack[-1]
        
        
