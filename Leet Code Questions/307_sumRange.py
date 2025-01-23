class NumArray:

    def __init__(self, nums: list[int]):
        n = len(nums)
        self.cpnums = nums[:]
        self.cpn = n
        self.prefix_sum = [0]*n
        self.prefix_sum[0] = nums[0]
        for i in range(1,n):
            self.prefix_sum[i] = self.prefix_sum[i-1] + nums[i]

    def update(self, index: int, val: int) -> None:
        prev = self.cpnums[index]
        diff = val - prev
        self.cpnums[index] = val
        for i in range(index, self.cpn):
            self.prefix_sum[i] += diff
        

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_sum[right]
        else:
            return (self.prefix_sum[right] - self.prefix_sum[left-1])


# Your NumArray object will be instantiated and called as such:
nums = [7,2,7,2,0]
obj = NumArray(nums)
obj.update(4,6)
obj.update(0,2)
obj.update(0,9)
obj.sumRange(4,4)
obj.update(3,8)
obj.sumRange(0,4)
obj.update(4,1)
obj.sumRange(0,3)
obj.sumRange(0,4)
obj.update(0,4)

print(obj)