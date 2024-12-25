#https://www.scaler.com/academy/mentee-dashboard/class/325310/homework/problems/5153?navref=cl_tt_lst_nm
def maxOccurrences(A, B):
    # Step 1: Sort the array
    A.sort()
    N = len(A)
    
    # Initialize variables
    max_count = 0
    min_number = float('inf')
    prefix_sum = [0] * N
    prefix_sum[0] = A[0]
    
    # Calculate prefix sums
    for i in range(1, N):
        prefix_sum[i] = prefix_sum[i - 1] + A[i]
    
    # Sliding window approach
    for i in range(N):
        low, high = 0, i
        while low <= high:
            mid = (low + high) // 2
            total_sum = A[i] * (i - mid + 1)
            current_sum = prefix_sum[i] - (prefix_sum[mid - 1] if mid > 0 else 0)
            required_operations = total_sum - current_sum
            
            if required_operations <= B:
                # Valid window
                count = i - mid + 1
                if count > max_count or (count == max_count and A[i] < min_number):
                    max_count = count
                    min_number = A[i]
                high = mid - 1
            else:
                low = mid + 1
    
    # Return the result as [max_count, min_number]
    return [max_count, min_number]

# Sample inputs
A = [2, 2, 2, 3, 3]
B = 3
print(maxOccurrences(A, B)) # [3, 2]

A = [1, 2, 2, 3, 3]
B = 3
print(maxOccurrences(A, B)) # [3, 2]