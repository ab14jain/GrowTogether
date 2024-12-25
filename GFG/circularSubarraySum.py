#https://www.geeksforgeeks.org/problems/max-circular-subarray-sum-1587115620/1

def circularSubarraySum(arr):    
    n = len(arr)
    global_max = arr[0]
    global_min = arr[0]
    curr_max = 0
    curr_min = 0
    total_sum = 0
    for i in range(n):
        num = arr[i]
        curr_max = max(num, curr_max + num)
        curr_min = min(num, curr_min + num)
        global_max = max(global_max, curr_max)
        global_min = min(global_min, curr_min)
        total_sum += num
        print(global_max, global_min, total_sum, curr_max, curr_min)
    if global_max < 0:
        return global_max    
    return max(global_max, total_sum - global_min)
print(circularSubarraySum([8,-8,9,-9,10,-11,12])) #22
print(circularSubarraySum([10, -3, -4, 7, 6, 5, -4, -1])) #23
print(circularSubarraySum([-10, -3, -4, -7, -6, -5, -4])) #-3