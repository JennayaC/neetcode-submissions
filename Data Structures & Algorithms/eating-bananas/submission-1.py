"""
Inputes:
1. Piles is an array of integers
2. Each num in array represents the number of bananas in a pile.
3. h is the number of hours given to eat all bananas. 

Output:
1. Integer that is the minimum bananas per hour eating rate to finish all bananas

Walkthgrough: broot force
1. Start with lowest minimal hour (choose lowest k) --> 1 banana/hour
2. Loop through the piles and accumulate hours (ceil(pile / k))
3. Get total hours to complete bananas
4. Ask is the total hours less or equal to than h?
5. If no, accumulate k by 1.
6. If yes return k

What we need:
1. Binary Search 
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        low = 1
        high = max(piles)

        while low < high:
            mid = (high + low) // 2

            hours = 0
            for pile in piles:
                hours += (pile+mid-1) // mid 
            
            if hours<=h:
                high = mid
            else:
                low = mid + 1
        return low

        

        