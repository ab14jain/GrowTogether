class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        return bin(x^y).count('1')

        # count = 0
        # arrX = list(bin(x)[2:])
        # arrY = list(bin(y)[2:])
        # arrX.reverse()
        # arrY.reverse()

        # print(arrX)
        # print(arrY)

        # x_len = len(arrX)
        # y_len = len(arrY)
        # min_len = min(x_len,y_len)

        # for i in range(min_len):
        #     if arrX[i] != arrY[i]:
        #         count += 1
        # if(x_len < y_len):
        #     count = count + y_len - min_len
        # elif(x_len > y_len):
        #     count = count + x_len - min_len
        # return count
        


s=Solution()

print(s.hammingDistance(1,4)) # 2
# print(s.hammingDistance(3,1)) # 1
# print(s.hammingDistance(3,3)) # 0
# print(s.hammingDistance(0,0)) # 0
# print(s.hammingDistance(0,1)) # 1
