#https://www.geeksforgeeks.org/problems/rotate-by-90-degree0356/1
def rotate(mat): 
    #code here
    row = len(mat)
    col = len(mat[0])  
    
    for c in range(col):
        i = 0
        j = row - 1
        while i < j:
            temp = mat[i][c]
            mat[i][c] = mat[j][c]
            mat[j][c] = temp
            
            i += 1
            j -= 1
    c = 0
    r = 0
    while c < col:
        r = c
        while r < row:
            temp = mat[c][r] 
            mat[c][r] = mat[r][c]
            mat[r][c] = temp
            r += 1
        c += 1
       
    
    return mat

# The following code is used to test the function
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate(mat)) # Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
mat = [[1, 2], [3, 4]]
print(rotate(mat)) # Output: [[3, 1], [4, 2]]
mat = [[1]]
print(rotate(mat)) # Output: [[1]]
mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(rotate(mat)) # Output: [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]gfg