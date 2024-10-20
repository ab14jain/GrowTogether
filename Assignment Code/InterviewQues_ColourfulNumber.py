class Solution:
	# @param A : integer
	# @return an integer
	def colorful(self, A):
            str_a = str(A)
            n = len(str_a)
            seen = []
            for i in range(n):
                seen.append(int(str_a[i]))
                product = int(str_a[i])
                if product in seen:
                    return 0
                for j in range(i+1, n):
                    product *= int(str_a[j])
                    if product in seen:
                        return 0
                    else:
                        seen.append(product)
            
            
            return 1

s = Solution()
print(s.colorful(3245)) # 1
print(s.colorful(324)) # 0
print(s.colorful(236)) # 0
