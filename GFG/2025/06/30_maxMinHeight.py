class Solution():
    def maxMinHeight(self, arr, k, w):
        # code here
        
        def binary_search(l, h, val):
            while l < h:
                mid = l + (h-l)//2

                if val == mid:
                    return mid
                elif val < mid:
                    h = mid-1
                else:
                    l = mid+1
            
            return mid
        

        arr.sort()

        

