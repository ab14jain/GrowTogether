# https://www.scaler.com/academy/mentee-dashboard/class/325334/assignment/problems/678?navref=cl_tt_nv
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):

        stack = []

        for par in A:            
            if par in "{([":
                stack.append(par)
            else:
                if len(stack) == 0:
                    return 0
                p = stack.pop()
                if ((p == "[" and par == "]") or (p == "(" and par == ")") or (p == "{" and par == "}")):
                    continue
                else:
                    return 0
        
        if len(stack) == 0:
            return 1
        else:
            return 0


s=Solution()
print(s.solve("{[()]}")) # 1
print(s.solve("{[}")) # 0
print(s.solve("{{{{")) # 0
print(s.solve("}}}")) # 0
print(s.solve("{{{{}}")) # 0
print(s.solve("{{{{}}}}")) # 1