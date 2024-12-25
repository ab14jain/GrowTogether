#https://www.scaler.com/academy/mentee-dashboard/class/325378/homework/problems/333?navref=cl_tt_nv

class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return a list of integers
	def dNums(self, A, B):
            n = len(A)
            if B > n:
                return []
            
            char_dict = {}
            i = 0
            while i < B:
                if A[i] in char_dict:
                    char_dict[A[i]] += 1
                else:
                    char_dict[A[i]] = 1
                i += 1
            

            result = [0]*(n - B + 1)

            j = B

            result[0] = len(char_dict)
            while j < n:
                if char_dict[A[j-B]] == 1:
                    del char_dict[A[j-B]]
                else:
                    char_dict[A[j-B]] -= 1
                
                if A[j] in char_dict:
                    char_dict[A[j]] += 1
                else:
                    char_dict[A[j]] = 1
                
                result[j-B+1] = len(char_dict)
                j += 1
            
            return result
    
            # count = 0
            # char_dict = {}
            # result = []
            # for i in range(B):
            #     if A[i] in char_dict:
            #         char_dict[A[i]] += 1
            #     else:
            #         char_dict[A[i]] = 1
            #         count += 1
            # result.append(count)
            
            # for i in range(B, len(A)):
            #     if char_dict[A[i-B]] == 1:
            #         count -= 1
            #     char_dict[A[i-B]] -= 1
                
            #     if A[i] in char_dict:
            #         char_dict[A[i]] += 1
            #         if char_dict[A[i]] == 1:
            #             count += 1
            #     else:
            #         char_dict[A[i]] = 1
            #         count += 1
            #     result.append(count)
            # return result


s=Solution()
A = [1, 2, 1, 3, 4, 3]
B = 3
print(s.dNums(A, B)) # Output: [2, 3, 3, 2]
A = [1, 1, 2, 2]
B = 1
print(s.dNums(A, B)) # Output: [1, 1, 1, 1]
A = [1, 2, 3, 4, 5]
B = 3
print(s.dNums(A, B)) # Output: [3, 3, 3]