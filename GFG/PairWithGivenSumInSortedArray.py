#https://www.geeksforgeeks.org/problems/pair-with-given-sum-in-a-sorted-array4940/1

class Solution:
    def countPairs (self, arr, target) : 
        #Complete the function

        n = len(arr)
        low = 0 
        high = n - 1

        count = 0
        while low < high:

            if arr[low] + arr[high] < target:
                low += 1
            elif arr[low] + arr[high] > target:
                high -= 1
            else:

                count1 = 0
                count2 = 0
                element1 = arr[low]
                element2 = arr[high]

                while low <= high and arr[low] == element1:
                    count1 += 1
                    low += 1
                
                while low <= high and arr[high] == element2:
                    count2 += 1
                    high -= 1

                if element1 == element2:
                    count += (count1 * (count1 - 1)) // 2                    
                else:
                    count += count1 * count2                    

        return count
    
s=Solution()
print(s.countPairs([1,1,1,1], 2)) #6
print(s.countPairs([1,2,3,4,5,6,7,8,9], 10)) #4
print(s.countPairs([1,1,1,1,1], 2)) #10
print(s.countPairs([-1, 1, 5, 5, 7], 6)) #3
print(s.countPairs([-1, 10, 10, 12, 15], 125)) #0


