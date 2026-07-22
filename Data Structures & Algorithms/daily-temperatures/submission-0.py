class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        myStack = []

        for i in range(len(temperatures)):

            while myStack and temperatures[i] > temperatures[myStack[-1]]:
                prevDay = myStack.pop()
                result[prevDay] = i - prevDay

            myStack.append(i)

        return result 