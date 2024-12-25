#https://www.scaler.com/academy/mentee-dashboard/class/313168/homework/problems/936?navref=cl_tt_nv
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):        

        # Approach 1 - Brute Force
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        # Intution:
        # 1. Find the binary representation of A.
        # 2. Find the next greater number than A which has the same number of bits.
        # 3. Find the previous smaller number than A which has the same number of bits.
        # 4. XOR of the next greater number and previous smaller number is the answer.


        # x = A - 1
        # y = A + 1        
        # while x > 0:            
        #     if x ^ A == x + A:
        #         break
        #     x -= 1

        # while y < (10 ** 9):
        #     if y ^ A == y + A:
        #         break
        #     y += 1

        # XOR = x ^ y
        # return XOR

        # Approach 1 - Brute Force
        # Time Complexity: O(1)
        # Space Complexity: O(1)

        # Intution:
        # 1. Find the binary representation of A.
        # 2. Find the next greater number than A which has the same number of bits.
        # 3. Find the previous smaller number than A which has the same number of bits.
        # 4. XOR of the next greater number and previous smaller number is the
        # answer


        # A + B = A ^ B + 2 * (A & B)
        # So need to find A and B such that A & B = 0 and A ^ B = A + B
        # A & B = 0 means that the bits of A and B should not overlap.
        # A ^ B = A + B means that the bits of A and B should not overlap.
        # So, A and B should be consecutive numbers.
        # So, the answer is the next greater number than A which has the same number of bits.
        # So, the answer is the next greater number than A which has the same number of bits.

        bin_arr = bin(A)[2:]   
        next_greater = 1 << len(bin_arr)
        # Find the next greater number than A which has the same number of bits. 
        previous_smaller = A ^ (next_greater - 1)        
        return next_greater ^ previous_smaller
    
# Driver code
s = Solution()
print(s.solve(5)) # 10
print(s.solve(10)) # 21
print(s.solve(15)) # 16
print(s.solve(20)) # 43
print(s.solve(5250677)) # 11526538
print(s.solve(11526538)) # 11526538
print(s.solve(2147483647)) # 2147483648
