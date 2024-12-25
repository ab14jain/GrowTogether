class Solution:
    def canChange(self, start: str, target: str) -> bool:
        
        n = len(start)

        i = 0
        j = 0

        while i < n or j < n:
            while i < n and start[i] == '_':
                i += 1
            while j < n and target[j] == '_':
                j += 1

            if i == n or j == n:
                return i == n and j == n

            if start[i] != target[j]:
                return False

            if start[i] == 'L' and i < j:
                return False
            
            if start[i] == 'R' and i > j:
                return False

            i += 1
            j += 1
        

        return True
               

        # n = len(start)
        # list_start = list(start)
        # left = 0
        # lspacecount = 0
        # right = n - 1
        # rspacecount = n -1

        # while lspacecount <= rspacecount:

        #     if list_start[lspacecount] == '_':
        #         lspacecount += 1
        #     elif list_start[lspacecount] == 'L':
        #         list_start[left],list_start[lspacecount] = list_start[lspacecount],list_start[left]
        #         left += 1
        #         lspacecount += 1
                
            
        #     if list_start[rspacecount] == '_':
        #         rspacecount -= 1
        #     elif list_start[rspacecount] == 'R':
        #         list_start[right],list_start[rspacecount] = list_start[rspacecount],list_start[right]
        #         right -= 1
        #         rspacecount -= 1  
                
          
            
        #     if "".join(list_start) == target:
        #         return True

        #     if lspacecount == 0 or rspacecount == n - 1:
        #         break

        # return False

# Time complexity: O(n)
# Space complexity: O(n)

# Example 1:
sol = Solution()
print(sol.canChange("_L__R__R_","L______RR")) # True
print(sol.canChange("L_R","R_L")) # False
print(sol.canChange("L_R","R_L")) # False
print(sol.canChange("R_L_","__LR")) # Flase
print(sol.canChange("_R","R_")) # False
print(sol.canChange("L_","L_")) # True
print(sol.canChange("_L","_L")) # True
print(sol.canChange("L_","_L")) # False
print(sol.canChange("____RL____","L________R")) # True
print(sol.canChange("_L__R__R_L","L______RR_")) # True