#https://www.geeksforgeeks.org/problems/kth-distance3757/1
class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        # your code
        n = len(arr)
        if n == 1: return False
        if n == 2:
            if arr[0] == arr[1]:
                return True        
            return False
        
        for i in range(n-k):
            j = 1
            curr_num = arr[i]
            while j <= k:
                if curr_num == arr[i + j]:
                    return True
                j += 1

        #within last k elements

        for i in range(n-k, n):
            j = 1
            curr_num = arr[i]
            while j <= k:
                if curr_num == arr[i - j]:
                    return True
                j += 1    
        
        return False


sol = Solution()   
# print(sol.checkDuplicatesWithinK([1, 2, 3, 4, 1, 2, 3, 4], 3)) # Output: True
# print(sol.checkDuplicatesWithinK([1, 2, 3, 1, 4, 5], 3)) # Output: True 

# s="19473 32296 19809 6699 922 6741 21952 31386 17646 16570 27820 15297 759 18538 15742 2537 28134 16799 29973 1471 28107 22014 12564 18099 11106 32284 28491 23711 6960 12352 4466 5289 16079 27755 18717 1386 4231 18837 32748 9808 19742 26682 4098 30272 4080 28181 24761 30080 30018 28460 15252"
# print(sol.checkDuplicatesWithinK(list(map(int, s.split())), 21)) # Output: False
s="1151 21166 5739 27396 19900 1085 1070 7084 18988 28398 595 19412 2608 19635 25046 19480 4415 29489 16789 8300 29137 4119 10583 16141 24699 32687 22028 15288 603 29107 6999 13081 31414 20577 32329 2694 31712 7633 28016 22509 24412 15239 14864 1547 2373 20549 14000 2271 6892 16418 7896 13919 14531 27360 11290 5993 26490 9339 31823 17660 17511 7166 11555 9640 7467 9370 20692 8003 10899 5369 8246 4318 29372 12496 3579 10487 5755 20660 7985 27633 3579 15406 11532 32449 6312 27153 29670 2537 25676 6923 4996 18602 12152"
print(sol.checkDuplicatesWithinK(list(map(int, s.split())), 82)) # Output: True