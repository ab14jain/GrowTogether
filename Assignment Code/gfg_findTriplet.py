#https://www.geeksforgeeks.org/problems/triplet-family/1
class Solution:
    def findTriplet(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(1, n):
                sum_t = arr[i] + arr[j]
                if sum_t in arr:
                    return True
        
        return False
    
# Driver code

s = Solution()
# arr = [1, 2, 3, 4, 5]
# print(s.findTriplet(arr)) # False
print(s.findTriplet([6865,8921, 22468, 20392, 27390, 31530, 8847, 26964,20505, 21692, 7535, 31540, 18233, 19549, 30152, 12717 ,28032, 25526, 23414, 7868, 26691, 22744, 18960, 28208,6250, 7192, 30569, 10775, 7450, 22557, 2909])) # False
