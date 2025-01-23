# https://www.geeksforgeeks.org/problems/count-distinct-elements-in-every-window/1
class Solution:
    def countDistinct(self, arr, k):
        # Code here

        n = len(arr)
        count_map = {}
        ans = []
        
        for i in range(k):
            if arr[i] not in count_map:
                count_map[arr[i]] = 1
            else:
                count_map[arr[i]] += 1
        
        ans.append(len(count_map))    
        m = 0
        if count_map[arr[m]] == 1:
            count_map.pop(arr[m])
        else:
            count_map[arr[m]] -= 1
        m += 1

        for i in range(k,n):
            if arr[i] not in count_map:
                count_map[arr[i]] = 1
            else:
                count_map[arr[i]] += 1

            ans.append(len(count_map))  
            if arr[m] in count_map:
                if count_map[arr[m]] == 1:
                    count_map.pop(arr[m])
                else:
                    count_map[arr[m]] -= 1      
            m += 1

            
        return ans

s=Solution()
print(s.countDistinct([1, 2, 1, 3, 4, 2, 3], 4)) #[3, 4, 4, 3]   
print(s.countDistinct([1, 2, 4, 4], 2)) #[2, 2, 1]
print(s.countDistinct([4, 1, 1], 2)) #[2, 1]
print(s.countDistinct([1, 1, 1, 1, 1], 3)) #[1, 1, 1]

str="1 2 4 5 3 3 2 1 2 4 6 7 8 98 9 67 5 43 3 3 45 5 6 67 5 43 3 2 2 2 3 54 65 6 7 7 7 5 4 3 4 6 7 78 78 8 8 6 5 5 54 4 4 4 43 22 2 344"
arr = list(map(int,str.split(" ")))
print(s.countDistinct(arr, 4)) #[   
            

