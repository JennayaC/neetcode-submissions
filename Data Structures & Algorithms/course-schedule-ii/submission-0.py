from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        waiting_count = {}

        unlocks = {}

        for i in range(numCourses):
            waiting_count[i] = 0
            unlocks[i] = []
        
        for prereque in prerequisites:
            before = prereque[1]
            after = prereque[0]
        
            unlocks[before].append(after)# make sure to append after before prereque

            waiting_count[after] += 1 #Accumulate by 1 if course comes after another class

        ready = deque()
        for i in range(numCourses):
            if waiting_count[i] == 0:
                ready.append(i)

        order = []

        while len(ready) > 0:
            completed = ready.popleft()
            order.append(completed)

            for next_course in unlocks[completed]:
                waiting_count[next_course] -= 1
                if waiting_count[next_course] == 0:
                    ready.append(next_course)
        
        if len(order) == numCourses:
            return order
        else:
            return []





        