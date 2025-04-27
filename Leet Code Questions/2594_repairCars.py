import math
from typing import List


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        l = 1
        r = min(ranks)*cars*cars      
        ans = 0
        def is_possible(time): 
            count = 0
            for i in range(len(ranks)):
                count += math.floor(math.sqrt(time//ranks[i]))            
                if count >= cars:
                    return True           

            return False
        
        while l <= r:
            mid = l + (r-l)//2
            if is_possible(mid):  
                ans = mid              
                r = mid - 1
            else:
                l = mid + 1

        return ans
    

s=Solution()
print(s.repairCars([4,2,3,1], 10))