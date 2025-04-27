#https://www.geeksforgeeks.org/problems/decode-the-string2444/1

class Solution:
    def decodedString(self, s):
        # code here

        stack = []
        i = 0
        n = len(s)
        while i < n: 
            if s[i] == ']':
                tempstr = []                
                curr = stack[-1]
                while stack and curr not in [0,1,2,3,4,5,6,7,8,9]:
                    stack.pop()
                    if curr == '[':                        
                        break
                    if ord(curr) >= 97 and ord(curr):
                        tempstr.append(curr)
                    curr = stack[-1]
                k = 0
                times = 0
                curr = stack[-1]
                while stack and curr in ['0','1','2','3','4','5','6','7','8','9']:
                    stack.pop()
                    k += int(curr) * (10**times)
                    times +=1
                    if stack:
                        curr = stack[-1]
                
                revtemp = "".join(tempstr[::-1])

                while k:
                    stack.extend(revtemp[:])
                    k -= 1
            else:
                stack.append(s[i])

            i += 1
        return "".join(stack)
    
s=Solution()

print(s.decodedString("101[b]"))
print(s.decodedString("101[b45[rtyhtfgh]656[dgfbxvx]]"))
print(s.decodedString("3[b2[ca]]"))
