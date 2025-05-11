from collections import Counter
class Solution:
    def maxLength(self, arr):
        # code here
        
        counter = Counter(arr)
        arr.sort()
        n = len(arr)
        plank_count = 0
        max_plank_size = float('-inf')
        required_plank = 0
        cpy = dict(counter)
        for i in range(n-1, -1, -1):
            counter = dict(cpy)
            count = counter[arr[i]]
            
            num = arr[i]
            plank_count = 0
            for j in range(n-count):
                countj = counter[arr[j]]
                if (num - arr[j]) in counter and counter[arr[(num - arr[j])]] > 0:
                    countn = counter[(num - arr[j])]
                    counter[(num - arr[j])] -= min(countj,countn)
                    plank_count = plank_count + min(countj,countn)
            
            planks = (count + plank_count)
            if max_plank_size < num * planks:
                max_plank_size =  num * planks
                required_plank = planks-1

        return required_plank
                

s=Solution()
# print(s.maxLength([1,3,2,5,2,5,4,2,1]))
print(s.maxLength([4,5,7,8,5,4,6,7,7,3,3]))