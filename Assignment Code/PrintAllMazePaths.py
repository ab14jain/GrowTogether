#https://www.scaler.com/academy/mentee-dashboard/class/325380/assignment/problems/125661?navref=cl_tt_lst_nm

class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of strings
    def PrintAllPaths(self, A, B):

        #path as array list to reduce string space taken multiple time
        
        #Time Complexity O(2^(n+m))
        #Space Complexity O(n+m)
        ans = []  
        def print_path(path, src_r, src_c, dest_r, dest_c):          
            
            if src_r == dest_r and src_c == dest_c:
                ans.append("".join(path))
                return
            
            if src_r < A-1:
                path.append('D')
                print_path(path, src_r+1, src_c, dest_r, dest_c)
                path.pop()                

            if src_c < B-1:    
                path.append('R')
                print_path(path, src_r, src_c+1, dest_r, dest_c)
                path.pop()          
        
        print_path([], 0, 0, A-1, B-1)

        return ans

        #path string space taken multiple time makes space complexity 
        # Space O(nm)
        # Time O(2^(n+m))

        # ans = []  
        # def print_path(path, src_r, src_c, dest_r, dest_c):          
            
        #     if src_r == dest_r and src_c == dest_c:
        #         ans.append("".join(path))
        #         return
            
        #     if src_r < A-1:                
        #         print_path(path+"D", src_r+1, src_c, dest_r, dest_c)

        #     if src_c < B-1:   
        #         print_path(path+"R", src_r, src_c+1, dest_r, dest_c)

        
        # print_path("", 0, 0, A-1, B-1)       

        # return ans


s=Solution()
print(s.PrintAllPaths(3,2))
print(s.PrintAllPaths(1,2))