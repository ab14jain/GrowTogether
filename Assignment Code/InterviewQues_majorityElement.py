class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        majority_element = 0
        count = 0

        for i in A:
            if count == 0:
                majority_element = i
                count = 1
            elif majority_element == i:
                count += 1
            else:
                count -= 1
        
        return majority_element