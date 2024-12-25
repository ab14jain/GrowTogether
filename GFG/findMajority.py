#https://www.geeksforgeeks.org/problems/majority-vote/1

class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.

        if len(arr) == 1:
            return arr

        majority_1 = arr[0]
        majority_2 = arr[1]
        count_1 = 0
        count_2 = 0

        n = len(arr)


        for i in range(n):

            if arr[i] == majority_1:
                count_1 += 1            
            elif arr[i] == majority_2:
                count_2 += 1
            elif count_1 == 0 and arr[i] != majority_2:
                majority_1 = arr[i]
                count_1 = 1
            elif count_2 == 0 and arr[i] != majority_1:
                majority_2 = arr[i]
                count_2 = 1
            else:
                count_1 -= 1
                count_2 -= 1

        count_1 = 0
        count_2 = 0

        for i in range(n):
            if arr[i] == majority_1:
                count_1 += 1
            elif arr[i] == majority_2:
                count_2 += 1
        ans = []
        if count_1 > n // 3:   
            ans.append(majority_1)
        if count_2 > n // 3:
            ans.append(majority_2)

        return ans

s=Solution()
print(s.findMajority([3,1,3,3,2,2,2])) #3
print(s.findMajority([1])) #[1]
print(s.findMajority([1,2])) #[1,2]
print(s.findMajority([2,1])) #[1,2]
print(s.findMajority([1,2,3])) #[]
print(s.findMajority([1,2,3,1,1])) #1
print(s.findMajority([1,2,3,1,1,2,2])) #[1,2]

   