
#https://www.geeksforgeeks.org/problems/pair-in-array-whose-sum-is-closest-to-x1124/1
class Solution:
    def sumClosest(self, arr, target):
        # code here

        #Approach: Sort the array and use two pointers to find the pair
        arr.sort()
        n = len(arr)
        low = 0
        high = n - 1       
        ans = []  

        abs_diff = float('inf') 

        while low < high:
            calc = arr[low] + arr[high]

            if abs(target - calc) < abs_diff:
                abs_diff = abs(target - calc)
                ans = [arr[low], arr[high]]
                        
            if calc < target:
                low += 1
            elif calc > target:        
                high -= 1   
            else:
                return [arr[low], arr[high]]               

        return ans
    
    # Approach 2: Sort then use binary search to find the closest sum
    

s=Solution()
print(s.sumClosest([5,2,7,1,4], 10))
print(s.sumClosest([10,30,20,5], 25))
print(s.sumClosest([10], 10))
        

        