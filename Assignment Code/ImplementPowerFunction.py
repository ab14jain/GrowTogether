import sys
sys.setrecursionlimit(10**9)
# Do not write code to include libraries, main() function or accept any input from the console.
# Initialization code is already written and hidden from you. Do not write code for it again.
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def pow(self, A, B, C):
        # Just write your code below to complete the function. Required input is available to you as the function arguments.
        # Do not print the result or any output. Just return the result via this function.

        def powA(A, B, C):            
            if B == 0:
                return 1
            
            if B % 2 == 0:
                calc = powA(A, B//2, C)
                calc = (calc * calc) % C
            else:
                calc = powA(A, (B-1)//2, C)
                calc = (calc * calc * A ) % C            
            return calc

        if A == 0:
            return 0
        elif A > 0:
            A = A % C        
        else:
            while A > 0:
                A = A + C
            A = A % C    

        calc = powA(A, B, C) % C
        return calc
    

# You have to implement the following function. You can add any helper function you want in the class.



s=Solution()
# print(s.pow(-9,3,90)) # 81
print(s.pow(71045970,41535484,64735492))
# print(s.pow(247456,345645,356756)) # 2
# print(s.pow(2,3,5)) # 3
# print(s.pow(2,3,7)) # 1
# print(s.pow(2,3,9)) # 8
# print(s.pow(2,3,10)) # 8
# print(s.pow(2,3,11)) # 8