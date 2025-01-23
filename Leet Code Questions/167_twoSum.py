class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        
        n = len(numbers)
        i = 0
        j = n - 1

        while i < j:
            calc = numbers[i] + numbers[j]
            if calc == target:
                return [i+1,j+1]
            elif calc > target:
                j -= 1
            else:
                i += 1

        return [-1,-1]