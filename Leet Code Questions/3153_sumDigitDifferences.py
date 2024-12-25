class Solution:
    def sumDigitDifferences(self, nums: list[int]) -> int:
        n = len(nums)  
        sum_digit = 0     
        for d in range(len(str(nums[0]))):                
            for i in range(10):                     
                # print("=======================================")
                # print(i)  
                a = 0     
                for num in nums:
                    str_arr = str(num)
                    if str_arr[d] == str(i):
                        # print(num)
                        a += 1
                b = n - a
                sum_digit += a*b
                # print("=======================================")
        return sum_digit//2
    

s=Solution()
# print(s.sumDigitDifferences([10,10,10,10])) # 0
print(s.sumDigitDifferences([13,23,12,33])) # 4
print(s.sumDigitDifferences([1045,3410,8910,6710])) # 4
print(s.sumDigitDifferences([34513,23742,12454,45897,60975,46565,37842,13421,47892,54567,23486,21330,12386,25493])) # 4
# print(s.sumDigitDifferences([1,2,3,4,5,6,7,8,9])) # 0
# print(s.sumDigitDifferences([42,11,1,97])) # 3
# print(s.sumDigitDifferences([42,33,60])) # 3
# print(s.sumDigitDifferences([42,33,60,1])) # 4
# print(s.sumDigitDifferences([42,33,60,1,0])) # 5