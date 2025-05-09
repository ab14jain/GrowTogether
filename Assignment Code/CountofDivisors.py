#https://www.scaler.com/academy/mentee-dashboard/class/325296/assignment/problems/4107?navref=cl_tt_nv


from math import ceil, sqrt


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        big_int = 1000005
        spf = [1]*big_int

        for i in range(1, big_int):
            spf[i] = i

        sqrt_val = ceil(sqrt(big_int))
        for i in range(2,sqrt_val+1):
            for j in range(i*i,big_int, i):
                if spf[j] == j:
                    spf[j] = i

        n = len(A)
        res = []
        for i in range(n):
            temp = A[i]
            ans = 1

            while temp != 1:
                count = 1
                d = spf[temp]
                while temp != 1 and temp%d == 0:
                    count += 1
                    temp //= d

                ans *= count
            
            res.append(ans)
        return res

        # n = len(A)
        # if n == 1 and A[0] == 1:
        #     return 1
        # max_A = max(A)
        # shieve = [2]*(max_A+2)
        # shieve[0] = 0
        # shieve[1] = 1

        # # for i in range(2,max_A):
        # #     for j in range(2,(max_A//i)+1):
        # for i in range(2,max_A//2+1):
        #     for j in range(2*i,max_A+1,i):
        #         num = j
        #         shieve[num] += 1
        
        # ans = []

        # for num in A:
        #     ans.append(shieve[num])
        
        # return ans

        # def calc_smallest_prime_factor(num):
        #     large_num = min(1000000,num)
        #     smallest_prime_factor = [0]*large_num

        #     for i in range(1,large_num):
        #         smallest_prime_factor[i] = i
            
        #     for i in range(2,math.ceil(math.sqrt(large_num))):
        #         for j in range(i*i,large_num,i):
        #             if smallest_prime_factor[j] == j:
        #                 smallest_prime_factor[j] = i  
            
        #     return smallest_prime_factor

        # result = []
        # a_size = len(A)
        # max_A = max(A)
        
        # if max_A < 100000:
        #     smallest_prime_factor = calc_smallest_prime_factor(max_A+1)
        # else:
        #     smallest_prime_factor = calc_smallest_prime_factor(1000000)
        
        # for i in range(a_size):
        #     temp = A[i]
        #     ans = 1
        #     while temp != 1:
        #         cnt = 1
        #         d = smallest_prime_factor[temp]
        #         while temp != 1 and temp % d == 0:
        #             cnt += 1
        #             temp //= d
                
        #         ans *= cnt
            
        #     result.append(ans)

        # return result

        # def SieveOfEratosthenes(n, prime,primesquare, a): 
        #     # Create a boolean array "prime[0..n]"  
        #     # and initialize all entries it as  
        #     # true. A value in prime[i] will finally  
        #     # be false if i is not a prime, else true. 
        #     for i in range(2,n+1): 
        #         prime[i] = True
        
        #     # Create a boolean array "primesquare[0..n*n+1]" 
        #     # and initialize all entries it as false.  
        #     # A value in squareprime[i] will finally be  
        #     # true if i is square of prime, else false. 
        #     for i in range((n * n + 1)+1): 
        #         primesquare[i] = False
        
        #     # 1 is not a prime number 
        #     prime[1] = False
        
        #     p = 2
        #     while(p * p <= n): 
        #         # If prime[p] is not changed,  
        #         # then it is a prime 
        #         if (prime[p] == True): 
        #             # Update all multiples of p 
        #             i = p * 2 
        #             while(i <= n): 
        #                 prime[i] = False
        #                 i += p 
        #         p+=1
            
        
        #     j = 0
        #     for p in range(2,n+1):  
        #         if (prime[p]==True):  
        #             # Storing primes in an array 
        #             a[j] = p 
        
        #             # Update value in primesquare[p*p], 
        #             # if p is prime. 
        #             primesquare[p * p] = True
        #             j+=1
        
        # # Function to count divisors 
        # def countDivisors(n): 
        #     # If number is 1, then it will 
        #     # have only 1 as a factor. So, 
        #     # total factors will be 1. 
        #     if (n == 1): 
        #         return 1
        
        #     prime = [False]*(n + 2) 
        #     primesquare = [False]*(n * n + 2) 
            
        #     # for storing primes upto n 
        #     a = [0]*n 
        
        #     # Calling SieveOfEratosthenes to  
        #     # store prime factors of n and to  
        #     # store square of prime factors of n 
        #     SieveOfEratosthenes(n, prime, primesquare, a) 
        
        #     # ans will contain total 
        #     # number of distinct divisors 
        #     ans = 1
        
        #     # Loop for counting factors of n 
        #     i=0
        #     while(1):  
        #         # a[i] is not less than cube root n 
        #         if(a[i] * a[i] * a[i] > n): 
        #             break
        
        #         # Calculating power of a[i] in n. 
        #         cnt = 1 # cnt is power of  
        #                 # prime a[i] in n. 
        #         while (n % a[i] == 0): # if a[i] is a factor of n 
        #             n = n / a[i] 
        #             cnt = cnt + 1 # incrementing power 
        
        #         # Calculating number of divisors 
        #         # If n = a^p * b^q then total  
        #         # divisors of n are (p+1)*(q+1) 
        #         ans = ans * cnt 
        #         i+=1
        
        #     # if a[i] is greater than 
        #     # cube root of n 
            
        #     n=int(n) 
        #     # First case 
        #     if (prime[n]==True): 
        #         ans = ans * 2
        
        #     # Second case 
        #     elif (primesquare[n]==True): 
        #         ans = ans * 3
        
        #     # Third case 
        #     elif (n != 1): 
        #         ans = ans * 4
        
        #     return ans # Total divisors 
        
        # res = []
        # n = len(A)
        # for i in range(n):
        #     res.append(countDivisors(A[i]))

        # return res


s=Solution()
print(s.solve([97,100,120,34,56,64]))
print(s.solve([100000]))
print(s.solve([1000000]))
print(s.solve([210000]))
print(s.solve([2,3,4,5]))
print(s.solve([8,9,10]))
print(s.solve([2,3,4,5,6,10,25]))

str = "2 8 2 48 4 8 48 16 4 2 8 16 4 12 48 32 4 4 24 8 24 2 4 8 6 32 48 16 8 2 108 4 4 8 12 8 24 40 12 4 4 16 12 12 8 24 4 24 32 2 24 24 4 8 18 24 48 2 8 144 60 36 4 16 16 4 4 6 8 8 2 20 4 4 32 12 4 40 12 16 4 16 4 16 8 4 128 6 6 8 8 12 24 8 8 8 16 24 16 24 8 12 4 4 48 8 2 16 4 16 12 8 4 36 30 2 4 4 12 2 4 24 8 24 8 4 24 24 8 24 24 4 8 16 4 36 16 4 8 32 24 6 8 8 4 4 2 8 2 48 4 36 30 8 4 8 8 24 36 72 4 2 32 8 6 6 4 64 6 12 4 120 8 4 16 24 16 12 8 4 4 48 6 4 8 2 8 8 8 16 28 32 16 4 4 16 4 6 12 8 8 24 32 4 64 2 4 8 16 4 16 32 12 4 48 2 16 16 12 12 6 4 4 8 16 4 8 4 16 4 24 36 2 12 8 8 8 8 4 12 60 12 4 12 12 2 8 4 4 20 4 2 8 4 4 12 120 8 8 4 4 16 40 4 24 8 8 2 4 8 4 16 4 4 10 32 12 12 2 96 4 12 16 4 12 4 4 24 4 32 8 8 8 12 4 4 8 12 16 24 16 4 16 32 4 4 64 6 32 8 20 16 6 6 120 56 16 4 8 24 40 12 8 12 8 4 8 24 4 16 16 8 6 6 28 24 12 16 16 8 2 2 8 4 20 8 8 12 2 16 4 4 8 16 24 24 8 2 24 8 16 4 8 16 4 8 24 4 2 40 8 6 6 16 16 8 24 48 16 8 16 16 80 16 32 24 4 8 4 12 16 4 8 2 8 24 8 8 80 12 6 4 8 4 16 8 4 8 8 40 6 4 8 24 12 48 8 16 4 4 60 10 12 40 2 2 32 16 10 8 4 6 4 4 12 8 4 4 6 4 16 12 8 8 8 16 16 24 8 4 16 16 24 2 2 8 16 48 8 16 4 16 8 8 4 12 24 8 30 16 4 32 4 4 4 8 144 24 2 2 6 8 48 8 8 8 32 8 2 12 8 2 4 4 24 24 40 8 64 12 8 16 8 48 4 32 4 96 4 8 8 4 24 4 4 8 4 4 8 12 16 8 4 2 10 8 48 24 16 8 24 8 12 8 4 12 12 4 8 24 4 8 12 32 8 48 8 12 32 24 2 40 8 16 16 64 32 32 16 4 8 2 4 20 8 12 8 4 12 4 12 2 24 4 16 4 6 16 60 2 4 16 24 12 24 8 20 16 8 16 2 4 8 32 16 36 24 8 16 8 4 8 4 4 20 4 16 4 2 16 16 24 32 8 4 32 8 48 16 4 32 24 8 2 32 12 12 2 4 2 8 20 32 16 2 4 8 64 2 8 2 16 8 2 8 16 12 80 6 24 8 32 16 4 8 2 6 16 6 80 14 2 4 8 24 4 24 84 12 4 16 8 20 2 8 16 96 4 4 12 12 4 24 4 4 12 2 4 8 8 2 8 16 6 8 4 120 8 2 16 2 16 16 16 16 8 8 16 12 4 12 16 4 6 20 24 16 8 4 16 2 10 16 4 8 4 4 8 4 16 4 16 8 4 4 28 20 32 8 16 8 16 24 8 16 2 8 8 12 16 64 4 32 8 16 6 12 24 8 2 56 16 4 4 4 2 16 4 8 48 8 16 4 12 40 4 4 72 12 8 16 16 4 8 24 8 16 4 12 8 24 32 24 16 12 2 4 2 12 4 4 2 4 16 6 8 8 16 8 8 96 4 8 4 12 16 120 20 8 16 2 6 24 8 4 16 8 8 4 2 16 12 32 12 10 48 12 12 4 8 8 24 24 4 16 12 16 16 8 24 72 8 16 12 16 16 4 8 56 8 32 32 2 16 48 8 4 16 12 16 2 28 16 4 4 4 20 4 16 16 4 12 16 8 40 4 4 16 16 6 12 4 8 6 24 16 6 36 8 32 8 16 4 16 2 32 4 2 4 16 24 20 12 8 16 2 8 4 6 16 8 16 4 4 8 48 24 16 20 12 4 4 8 2 18 4 24 4 12 4 12 16 4 4 12 8 10 48 2 8 16 4 8 36 2 16 2 4 8 8 24 6 4 8 4 8 40 2 8 4 4 8 2 8 8 32 32 48 8 16 4 4 2 16 2 16 16 4 8 24 16 16 16 4 72 48 64 8 4 16 8 16 8 8 12 36 12 6 8 4 4 2 4 8 12 72 36 8 8 6 4 8 4 8 16 16 12 24 8 12 24 64 2 36 20 16 4 8 12 4 24 10 4 16 32 12 8 2 16 8 16 72 24 16 40 4 8 36 16 2 2 24 32 2 36 36 4 6 64 6 4 16 4 12 8 8 16 8 6 16 8 16 8 32 4 8 4 2 4 16 8 8 8 16 24 4 32 16 4 4 16 8 8 4 4 16 16 4 12 16 4 6 6 4 8 16 4 24 8 8 16 8 4 8 4 4 24 32 32 48 8 16 4 16 16 16 54 32 24 2 32 8 80 6 24 32 2 8 6 48 8 16 12 4 48 4 2 16 32 24 8 16 8 24 16 8 64 48 8 4 2 4 8 4 4 4 16 2 24 4 16 24 12 16 4 8 6 8 8 4 4 8 4 56 4 8 4 8 16 12 2 12 8 32 24 16 8 12 4 20 8 8 192 4 24 24 16 6 8 8 4 24 12 16 2 32 4 2 64 16 2 8 16 2 8 12 32 4 4 16 8 4 40 48 2 8 24 4 8 24 64 2 16 16 4 4 16 8 4 4 8 8 40 4 16 4 16 20 4 8 8 16 12 4 36 12 16 24 4 8 24 16 2 6 8 4 24 72 8 24 8 8 2 6 8 4 4 8 20 4 72 16 8 36 6 54 8 32 4 12 10 64 16 2 16 24 16 4 2 2 4 24 8 48 8 8 16 16 16 32 8 4 40 6 12 16 2 24 48 12 12 8 12 8 10 4 16 8 2 4 4 2 12 8 4 36 16 4 12 8 16 12 8 2 4 8 8 64 12 4 16 4 4 8 48 12 12 8 8 4 6 12 2 8 4 2 8 8 12 32 16 84 8 16 4 24 2 4 16 16 4 2 8 4 8 20 36 24 28 8 12 12 32 2 2 24 8 8 8 96 16 96 4 16 4 8 4 4 2 16 4 8 12 8 8 12 8 6 6 64 16 4 24 8 16 4 16 8 32 12 16 36 4 90 56 16 16 8 36 8 4 24 12 4 12 8 8 8 6 56 8 8 4 64 12 8 4 40 32 16 8 100 8 4 8 40 18 4 10 40 42 12 32 4 4 16 4 64 2 128 10 8 4 4 2 12 12 16 12 4 24 8 28 16 24 20 4 16 4 4 8 32 8 8 16 8 60 16 12 12 16 12 24 20 6 16 8 8 8 18 4 8 32 16 8 6 8 32 4 24 2 24 48 2 24 2 8 4 12 16 8 8 18 48 16 8 12 4 4 10 12 16 4 8 16 4 4 4 24 16 4 48 4 20 8 10 4 2 4 2 36 4 6 4 4 16 16 6 2 12 4 4 16 12 6 8 4 2 4 8 8 2 36 24 16 8 2 12 32 4 4 8 16 16 16 8 4 8 16 8 16 6 12 4 2 8 16 12 8 4 12 8 16 8 8 8 2 48 48 16 8 4 2 24 8 8 2 2 8 16 8 12 4 8 30 12 24 4 16 4 8 4 8 40 2 48 2 12 16 16 2 4 64 2 2 16 32 24 16 8 8 12 2 48 20 8 4 32 8 16 36 48 4 24 2 6 8 12 4 8 20 12 8 18 24 32 16 2 4 4 24 4 96 8 12 4 16 56 8 4 12 8 4 96 16 32 12 12 4 16 72 12 2 8 4 16 20 8 8 8 72 8 4 4 64 12 2 2 4 12 16 4 8 4 8 8 8 8 4 192 16 4 32 2 12 16 24 64 12 84 24 8 4 8 8 2 48 4 4 8 28 8 12 4 6 4 2 16 8 2 16 4 8 8 96 12 8 4 2 8 4 8 4 2 8 4 32 6 16 32 8 4 16 2 12 40 8 64 12 16 4 16 4 36 20 8 16 8 8 8 16 4 8 4 8 8 12 8 4 8 16 96 2 12 16 4 6 16 4 6 4 96 16 12 16 2 16 16 8 16 4 4 8 16 24 2 4 24 8 16 8 32 12 12 8 6 48 24 4 4 8 16 8 4 12 16 4 2 16 8 8 24 12 32 4 16 32 4 24 12 6 4 16 4 4 6 12 6 8 24 8 8 4 4 12 6 8 2 16 4 20 32 18 2 24 4 2 4 16 4 24 16 16 16 32 10 16 8 8 4 4 48 8 4 2 12 4 16 8 2 4 8 12 48 4 2 8 12 8 32 16 4 32 32 20 16 16 24 24 24 8 24 8 6 4 14 4 8 12 8 8 2 2 8 16 2 2 2 6 4 24 8 8 8 6 16 28 24 2 16 4 32 8 32 8 8 12 16 96 6 36 8 6 30 8 2 4 4 8 24 28 12 12 32 16 4 8 8 4 2 8 16 2 8 4 8 12 8 6 4 4 16 16 6 16 8 24 4 2 4 12 48 8 20 4 12 8 8 8 4 12 4 8 32 2 24 72 16 8 36 8 80 18 8 8 8 40 6 12 4 8 8 4 2 8 48 8 24 2 2 6 16 6 4 6 8 16 8 12 4 8 32 12 8 4 8 2 16 24 16 8 6 8 24 2 16 16 24 24 30 48 12 4 2 10 8 4 16 6 144 16 4 4 12 12 8 8 72 24 36 4 48 48 2 24 8 8 2 8 40 12 6 16 8 36 8 6 24 16 4 4 4 4 16 16 4 8 4 24 8 8 48 12 32 12 32 16 16 8 4 2 16 64 4 48 4 16 16 42 16 8 16 8 24 8 8 16 48 8 16 4 20 4 4 12 16 16 12 48 4 6 8 6 18 12 4 6 12 18 4 12 6 2 8 16 32 2 12 20 2 64 16 8 24 8 8 2 24 2 12 8 8 64 48 8 8 24 12 6 2 8 4 16 12 8 8 4 4 6 32 12 12 4 8 8 24 48 36 14 2 32 2 2 6 2 8 8 8 12 18 8 12 4 12 4 96 6 2 8 8 40 48 24 12 4 12 12 16 24 64 20 12 4 12 2 20 24 4 8 4 12 8 4 30 16 4 8 4 32 8 2 8 48 4 16 32 4 8 12 12 2 18 2 8 2 4 8 24 2 8 8 4 4 32 8 4 24 16 12 16 10 8 16 8 12 8 8 4 16 40 4 8 16 12 16 6 24 32 4 4 4 4 6 24 24 4 32 8 4 8 8 16 8 8 24 12 8 12 4 16 2 6 8 20 4 20 128 36 8 24 16 12 4 8 24 16 8 4 4 48 16 8 8 4 8 4 24 4 16 112 2 12 96 12 4 4 16 64 16 16 4 2 4 8 6 8 8 16 16 6 8 16 4 8 64 4 2 8 24 16 4 8 20 24 8 32 8 8 4 24 20 12 36 4 8 6 12 8 40 2 8 16 2 8 24 12 4 24 4 24 8 8 16 8 8 24 12 12 32 8 16 24 2 8 8 18 40 10 48 8 12 4 4 8 8 6 16 12 8 16 8 12 8 128 12 6 8 16 12 4 16 8 32 8 16 16 16 16 8 4 24 2 4 8 20 8 24 16 24 4 64 4 16 2 12 4 12 8 12 16 16 6 4 36 12 16 8 8 2 16 24 4 2 16 4 4 4 8 16 16 8 12 4 12 12 8 14 4 8 24 8 8 8 8 24 32 16 4 4 16 16 32 18 32 12 32 36 8 10 8 16 8 24 32 16 14 4 8 18 12 16 24 48 4 2 2 4 12 2 16 8 16 4 8 18 8 32 32 4 48 4 16 4 16 30 24 32 10 16 16 16 10 12 8 6 16 4 10 12 12 32 24 4 8 24 4 12 16 16 8 8 16 2 18 4 6 16 24 6 24 30 8 4 8 16 24 8 16 32 8 8 4 6 12 4 6 8 4 4 12 8 24 72 16 24 12 24 32 8 6 40 6 12 32 32 8 4 2 16 4 4 8 4 24 8 8 8 4 16 4 16 4 16 2 4 24 4 4 6 8 32 8 8 4 6 12 8 16 4 24 12 32 40 8 2 16 8 12 12 8 12 4 4 6 4 4 8 4 2 8 4 2 40 16 8 16 2 12 8 4 8 8 24 24 4 4 4 4 2 4 2 4 24 72 8 8 16 4 12 8 2 16 48 18 40 8 4 16 8 8 4 48 2 6 2 24 4 32 8 4 16 8 4 16 2 16 20 4 48 4 4 24 20 32 4 4 8 4 8 10 16 16 8 16 8 8 12 48 2 16 8 16 16 16 8 32 4 12 8 8 16 8 8 8 8 30 8 12 4 2 16 4 16 8 2 12 8 16 6 16 6 8 6 32 16 24 8 54 60 16 8 24 4 4 8 4 4 24 4 16 24 8 8 2 32 8 4 32 8 4 16 24 4 8 2 40 12 30 128 16 24 2 4 8 6 2 6 2 4 4 48 4 40 4 2 8 32 8 8 6 2 8 8 40 12 8 64 12 6 16 16 8 12 32 8 16 16 12 24 4 12 8 2 40 8 8 2 72 12 8 4 4 48 24 4 2 4 2 4 12 4 4 4 8 12 6 2 12 4 4 4 8 4 4 4 6 12 4 4 16 8 12 4 24 40 8 24 24 8 12 24 16 8 6 30 48 16 60 16 8 8 4 8 4 32 4 2 8 4 4 20 8 12 120 24 8 16 4 24 16 4 12 42 12 4 12 8 4 4 64 4 24 16 32 4 16 48 60 12 4 6 2 12 12 4 2 8 2 2 40 32 8 8 4 4 16 12 4 16 12 32 8 48 16 18 6 4 4 12 12 16 4 72 4 8 4 4 8 4 2 8 32 4 4 16 12 12 4 16 8 12 4 8 8 8 32 4 16 2 8 8 4 8 48 12 8 10 32 12 24 6 4 4 4 8 48 2 8 4 8 12 4 48 12 4 32 8 16 32 16 32 16 4 16 8 24 4 4 4 4 4 8 8 4 8 18 16 4 8 16 4 12 36 8 12 4 4 4 16 24 8 4 24 16 112 4 16 24 40 4 8 48 4 16 20 24 4 8 16 8 8 6 8 16 6 2 8 8 16 12 32 2 8 16 16 32 4 24 24 8 4 4 8 8 2 64 24 6 2 4 8 8 8 4 48 54 2 40 48 4 12 4 4 8 4 16 4 36 8 12 4 6 32 32 4 8 24 28 18 8 4 4 4 8 32 12 4 80 8 4 2 8 4 8 48 18 4 32 8 24 12 4 8 2 2 20 8 8 8 4 16 16 4 6 24 12 8 4 16 4 12 8 24 40 32 4 16 8 12 4 12 32 4 8 2 16 96 6 32 32 22 8 40 4 4 4 8 16 16 48 4 4 8 4 24 4 8 32 8 4 2 8 4 2 4 8 4 8 2 8 12 8 16 4 4 8 16 48 4 28 4 12 4 6 8 48 4 8 20 8 2 4 2 32 16 4 4 8 32 16 16 16 12 10 2 12 16 20 24 16 8 18 12 4 20 32 8 12 16 4 4 8 12 2 64 12 4 4 16 12 4 24 12 6 8 4 4 8 24 4 12 4 16 40 8 8 16 8 8 4 32 2 18 12 16 2 8 8 4 8 8 8 8 12 2 32 16 8 8 4 2 16 8 8 16 32 2 4 8 16 16 24 32 8 4 8 12 16 4 24 64 64 4 8 8 36 16 16 4 8 20 40 16 20 8 4 4 2 8 4 4 24 4 8 32 16 8 8 8 8 8 4 64 48 16 8 4 16 24 36 8 60 32 4 4 12 8 4 8 108 8 12 10 6 4 64 2 8 8 16 10 8 8 20 2 4 32 6 8 12 16 4 2 4 8 6 16 12 24 8 16 4 4 24 32 24 16 16 12 8 8 12 4 2 4 60 16 12 16 8 2 12 4 12 16 24 30 4 4 4 20 4 12 8 16 12 8 16 8 32 24 12 8 28 40 12 12 32 8 8 6 4 32 6 8 8 8 16 8 8 8 96 8 4 2 2 4 80 4 4 16 4 4 8 4 48 8 16 16 48 12 8 16 2 4 16 24 8 8 12 12 80 8 48 24 48 4 8 6 8 32 12 4 8 4 4 2 16 24 20 24 24 18 32 4 40 8 8 16 20 6 8 10 4 12 16 24 4 16 2 4 4 16 8 2 4 2 16 12 2 24 8 8 36 16 64 6 4 64 2 8 4 2 16 12 4 12 8 18 4 8 24 6 8 28 8 8 12 24 16 2 2 12 16 8 12 16 16 8 4 8 24 8 2 8 16 40 20 4 8 12 32 12 16 8 24 4 2 4 48 48 4 8 24 8 4 14 12 4 8 4 8 4 2 8 24 16 16 64 4 4 24 24 16 6 32 4 32 16 4 4 4 16 2 14 32 8 4 2 12 4 4 12 20 20 8 4 24 24 2 32 4 12 32 16 32 12 16 8 8 24 8 2 4 6 2 6 8 8 12 32 8 32 4 4 12 64 4 16 16 16 12 12 32 16 8 6 12 8 64 2 4 4 16 8 24 4 2 32 16 8 8 12 2 8 24 8 8 15 4 4 96 6 8 4 4 4 8 64 16 16 24 4 4 18 12 32 12 4 4 16 4 4 16 48 4 8 32 20 48 4 24 4 12 4 40 72 20 4 8 4 8 2 8 12 16 16 6 12 4 4 2 4 24 4 24 4 8 2 32 6 2 4 12 6 16 4 24 32 12 12 40 2 20 4 2 4 20 16 36 24 18 48 8 4 4 8 48 4 4 24 56 24 12 6 48 24 8 2 48 4 32 4 32 4 8 16 16 20 16 8 20 32 4 16 8 2 2 10 8 8 4 8 12 8 8 6 8 16 48 40 4 6 8 32 12 16 8 12 2 32 4 16 8 8 24 8 8 2 16 12 4 48 32 8 8 12 16 12 4 16 12 24 2 16 2 2 72 8 48 4 16 8 8 12 2 4 8 4 6 36 4 48 12 8 12 4 4 24 8 24 4 8 80 24 16 12 2 36"

news = list(map(int, str.split(" ")))
count = len(news)
#print(count)

print(s.solve(news))