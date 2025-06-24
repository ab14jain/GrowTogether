class Solution:
    def catchThieves(self, arr, k):
        #code  here

        n = len(arr)
        caught = [0]*n
        ans = 0
        for i in range(n):
            if arr[i] == 'P':
                j = i+1
                #Right side should be closet
                while j < n and j <= i+k:
                    if caught[j] == 0 and arr[j] == 'T':
                        caught[j] = 1
                        ans += 1
                        break
                    j += 1

                l = i-k
                while l < i and l >= 0:
                    if caught[l] == 0 and arr[l] == 'T':
                        caught[l] = 1
                        ans += 1
                        break
                    l += 1

        return ans
    
s=Solution()
# print(s.catchThieves(['T', 'T', 'P', 'P', 'T', 'P'], 2))
print(s.catchThieves(['P', 'T', 'T', 'P', 'T'], 1))
                
                
