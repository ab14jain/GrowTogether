#https://www.scaler.com/academy/mentee-dashboard/class/325350/assignment/problems/4035?navref=cl_tt_nv

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    A = int(input())
    dp = [-1]*(A+1)
    
    def fibonacci(n):

        first = 0
        second = 1

        if n == 0:
            return first
        
        if n == 1:
            return second
        
        if dp[n] != -1:
            return dp[n]
        
        dp[n] = fibonacci(n-1)+fibonacci(n-2)
        
        return dp[n]
    
    print(fibonacci(A))


    

if __name__ == '__main__':
    main()