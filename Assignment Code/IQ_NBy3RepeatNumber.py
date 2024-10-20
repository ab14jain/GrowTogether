class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        n = len(A)
        
        A_list = list(A)        
        first_count = 0
        second_count = 0
        i = 0
        first_majority = A_list[i]
        second_majority = -1
        while i < n:
            if first_majority == A_list[i]:
                first_count += 1
            elif second_majority == A_list[i]:
                second_count += 1
            elif first_count == 0:
                first_majority = A_list[i]
                first_count = 1
            elif second_count == 0:
                second_majority = A_list[i]
                second_count = 1
            else:
                first_count -= 1
                second_count -= 1 
            
            i += 1           


        freq_first = 0
        freq_second = 0
        for i in range(n):
            if A_list[i] == first_majority:
                freq_first += 1
            elif A_list[i] == second_majority:
                freq_second += 1
        
        if freq_first > n//3:
            return first_majority
        elif freq_second > n//3:
            return second_majority
            
        
        return -1                 
