import heapq


class Solution:
    def minSum(self, arr):
        # code here

        # min_heap: O(n)

        # num1, num2: O(n)

        # total in array_sum: O(n)

        # Other variables: O(1)

        def array_sum(arr1, arr2):            
            len1 = len(arr1)
            len2 = len(arr2)

            total = []
            carry = 0           

            for i in range(len2):
                t_sum = int(arr1[len1-i-1])+int(arr2[len2-i-1])+carry
                if t_sum > 9:
                    total.append(t_sum%10)
                    carry = 1
                else:
                    total.append(t_sum)
                    carry = 0
            if len(arr1) > len2 and int(arr1[0]):
                total.append(int(arr1[0]) + carry)
                carry = 0
            
            if carry == 1:
                total.append(1)

            ans = ''
            has_leading_zero = True
            for i in range(len(total)-1,-1,-1):
                if total[i] == 0 and has_leading_zero:
                    continue
                else:
                    ans += str(total[i])
                    has_leading_zero = False
                    
            
            return ans


        min_heap = []
        n = len(arr)

        for i in range(n):
            heapq.heappush(min_heap, arr[i])

        alternate = 0
        num1 = []
        num2 = []
        while min_heap:
            num = heapq.heappop(min_heap)
            if alternate:
                num2.append(str(num))
                alternate = 0
            else:
                num1.append(str(num))
                alternate = 1
        x=y=0
        if len(num1) > len(num2):
            return array_sum(num1, num2)
        else:
            return array_sum(num2, num1)            
        
    
s=Solution()
print(s.minSum([2, 4, 3, 5, 0, 0, 0, 8, 2, 9, 2]))
print(s.minSum([3,7,2]))
print(s.minSum([6, 8, 4, 5, 2, 3]))
print(s.minSum([5, 3, 0, 7, 4]))
print(s.minSum([9,4]))
print(s.minSum([5]))

