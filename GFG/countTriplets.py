class Solution:
    def countTriplets(self, arr, target):
        # code here

        n = len(arr)
        result = 0
        for i in range(n-2):
            first = arr[i]            
            j = i + 1
            k = n - 1
            while j < k:
                second = arr[j]
                third = arr[k]

                three_sum = first + second + third
                
                if three_sum < target:                    
                    j += 1
                elif three_sum > target:
                    k -= 1
                else:

                    second = arr[j]
                    third = arr[k]
                    count2 = 0
                    count3 = 0

                    while j <= k and arr[j] == second:
                        count2 += 1
                        j += 1
                    
                    while j <= k and arr[k] == third:
                        count3 += 1
                        k -= 1

                    if second == third:
                        result += count2 * (count2 - 1) // 2
                    else:
                        result += count2 * count3


        return result         
            


s=Solution()
print(s.countTriplets([-15, -7, -5, -4, 0, 1, 5, 7, 8, 20, 20], 1))
# print(s.countTriplets([-3,-1,-1,0,1,2], -2))
# print(s.countTriplets([-2, 0, 1, 1, 5], 1))