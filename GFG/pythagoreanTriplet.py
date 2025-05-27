#https://www.geeksforgeeks.org/problems/pythagorean-triplet3018/1


import math


class Solution:
	def pythagoreanTriplet(self, arr):
    	# code here

            # TLE 1010 / 1115
            # n = len(arr)
			
            # arr.sort()
            # for i in range(n):
            #     a = arr[i]
            #     for j in range(i+1, n):
            #         b = arr[j]
            #         for k in range(j+1,n):
            #             c = arr[k]
            #             if a*a+b*b == c*c:
            #                 return True
                        
            # return False
			
            # n = len(arr)

            # arr.sort()

            # for i in range(n):
            #     arr[i] = arr[i]*arr[i]
            

            # for i in range(n-1, 1, -1):                 
            #     l = 0
            #     r = i-1
            #     while l<r:
            #         if arr[l] + arr[r] == arr[i]:
            #             return True
            #         elif arr[l] + arr[r] < arr[i]:
            #             l += 1
            #         else:
            #             r -= 1

            # return False                  
			

            n = len(arr)
            maxC = 0
            for ele in arr:
                maxC = max(maxC, ele)

            # Visited array to mark the elements
            vis = [False] * (maxC + 1)

            # Marking each element of input array
            for ele in arr:
                vis[ele] = True

            # Iterate for all possible a
            for a in range(1, maxC + 1):

                # If a is not there
                if not vis[a]:
                    continue

                # Iterate for all possible b
                for b in range(1, maxC + 1):

                    # If b is not there
                    if not vis[b]:
                        continue

                    # calculate c value to form a pythagorean triplet
                    c = int(math.sqrt(a * a + b * b))

                    # If c^2 is not a perfect square or c exceeds the
                    # maximum value
                    if (c * c) != (a * a + b * b) or c > maxC:
                        continue

                    # If there exists c in the original array,
                    # we have found the triplet
                    if vis[c]:
                        return True

            return False


     

s=Solution()
print(s.pythagoreanTriplet([13, 9, 16, 3, 15, 8, 1, 28, 3, 12, 29, 3, 28, 19, 11, 25, 11, 26, 19, 3]))
# print(s.pythagoreanTriplet([3, 2, 4, 6, 5]))
# print(s.pythagoreanTriplet([3, 8, 5]))
# print(s.pythagoreanTriplet([1, 1, 1]))
		