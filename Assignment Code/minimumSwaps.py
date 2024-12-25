class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        window_size = 0
        for i in range(n):
            if A[i] <= B:                
                window_size += 1

        if window_size == 0 or window_size == n:
            return 0
        
        greater_than_B = 0
        current_window_swaps = window_size
        for i in range(n):            
            if A[i] > B:
                greater_than_B += 1            
           
            if i == window_size - 1:
                current_window_swaps = min(current_window_swaps, greater_than_B)
            elif i >= window_size:                
                if A[i - window_size] > B:
                    greater_than_B -= 1               
                
                current_window_swaps = min(current_window_swaps, greater_than_B)
        
        
        return current_window_swaps
    

        # max_count = 0
        # for i in range(n-window_size):
        #     count_in_curr_window = 0
        #     for j in range(i, i+window_size):
        #         if A[j] <= B:
        #             count_in_curr_window += 1
            
        #     if count_in_curr_window > max_count:
        #         max_count = count_in_curr_window
                
        
        # return window_size - max_count

        #need to find subarray of length count_lessthan with maximum number of elements less than B

        # [1, 12, 10, 3, 14, 10, 5]
        # [1, 0, 0, 2, 0, 0, 3]
        # [2, 7, 9, 8, 5, 7, 4]
        # [1, 0, 0, 0, 2, 0, 3]


        # no_of_swap = 0
        # i = 0
        # j = 0
        # while j < n:
        #     if A[i] < B:
        #         i += 1
        #         j += 1
        #     elif A[j] > B:
        #         j += 1
        #     elif A[j] < B:
        #         A[i], A[j] = A[j], A[i]
        #         i += 1
        #         j += 1
        #         no_of_swap += 1
        #     else:
        #         j += 1
        
        # return no_of_swap
    

s = Solution()            
print(s.solve([52,7,93,47,68,26,51,44,5,41,88,19,78,38,17,13,24,74,92,5,84,27,48,49,37,59,3,56,79,26,55,60,16,83,63,40,55,9,96,29,7,22,27,74,78,38,11,65,29,52,36,21,94,46,52,47,87,33,87,70], 19)) # 2
print(s.solve([1, 12, 10, 3, 14, 10, 5], 8)) # 2
print(s.solve([1, 3, 5, 2, 4, 6, 7], 5)) # 0
print(s.solve([1, 3, 5, 2, 4, 6, 7], 7)) # 2
print(s.solve([3,5,4,6,7], 1)) # 2
print(s.solve([1, 3, 5, 2, 4, 6, 7], 1)) # 0
print(s.solve([1, 3, 5, 2, 4, 6, 7], 2)) # 1
print(s.solve([1, 3, 5, 2, 4, 6, 7], 3)) # 0
