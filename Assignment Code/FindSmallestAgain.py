#https://www.scaler.com/academy/mentee-dashboard/class/325310/homework/problems/9155/submissions
import heapq


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        # n = len(A)
        # result = []
        # for i in range(n):
        #     for j in range(i+1,n):
        #         for k in range(j+1,n):
        #             result.append(A[i]+A[j]+A[k])
        
        # result.sort()
        # return result[B-1]

        # A.sort()
        # n = len(A)

        # min_heap = []

        # for i in range(n-2):
        #     for j in range(i+1,n-1):
        #         for k in range(j+1,n):                    
        #             heapq.heappush(min_heap, A[i]+A[j]+A[k])
                
        #             if len(min_heap) > B:
        #                 heapq.heappop(min_heap)  
        #             # min_heap.append(A[i]+A[j]+A[k])
        #             # if len(min_heap) > B:
        #             #     min_heap.remove(max(min_heap))

        # # return max(min_heap)                      
                    
        # return  heapq.heappop(min_heap)
    

        def count_triplets_with_sum_leq(A, target):
            """
            Helper function to count the number of triplets in A with a sum <= target.
            """
            N = len(A)
            count = 0
            for i in range(N - 2):
                left, right = i + 1, N - 1
                while left < right:
                    triplet_sum = A[i] + A[left] + A[right]
                    if triplet_sum <= target:
                        # All pairs between left and right form valid triplets
                        count += (right - left)
                        left += 1
                    else:
                        right -= 1
            return count


        def find_Bth_smallest_triplet_sum(A, B):
            """
            Finds the B-th smallest triplet sum in the array A.
            """
            A.sort()  # Sort the array
            N = len(A)

            # Define the range of possible triplet sums
            low = A[0] + A[1] + A[2]  # Minimum triplet sum
            high = A[N-3] + A[N-2] + A[N-1]  # Maximum triplet sum

            # Binary search to find the B-th smallest triplet sum
            while low < high:
                mid = (low + high) // 2
                if count_triplets_with_sum_leq(A, mid) < B:
                    low = mid + 1
                else:
                    high = mid

            return low
        
        return find_Bth_smallest_triplet_sum(A, B)



s=Solution()
print(s.solve([51302,46372,80785,57132,27280,19765,52432,4348,48520,45061,48036,47449,53229,83837,52671,51106,60060,85457,31324,40624,27068,39435,50855,67142,46450,70501,35801,62795,24183,57184,68389,43194,41553,40588,62293,47957,56153,52267,48180,45596,41088,70778,31658,45442,39121,79306,39082,53082,50877,49232,65483,46482,53009,51394,48569,35239,65478,24991,74569,52434,6787,61257,22383,43270,42712,43741,31440,56987,53325,59326,49462,50887,37922,61425,42152,40657,49876,68397,71252,36869,72027,33965,53556,43109,63030,50124,78445,47142,60972,19278,80758,18388,50383,45951,41468,39770,68800,62207,37256,62887,62390,35415,33503,69924,32316,58963,52516,33009,46909,68880,54472,61132,38721,59854,31774,27091,75636,52110,47563,14826,42090,59996,63717,60410,42149,34665,42711,35552,34517,64473,70406,47391,43993,51807,33846,40796,16529,34696,42920,58246,72531,44249,48651,40152,61748,43676,76305,30849,26385,52339,50396,66332,49738,50354,72736,51948,15694,62062,65029,20156,50139,46677,63185,60846,39682,27194,42050,19349,80109,53112,66235,56892,53343,67572,38951,38736,21503,28159,41109,57112,62806,57057,73896,54246,58258,19510,65966,66127,52752,42999,72594,35354,61084,32600,53361,58359,8054,22614,40462,48120,49428,42506,51431,70839,62379,26565,34084,42844,26730,50910,49460,78913,52874,51010,30261,14446,73740,57041,74264,48077,53813,67436,20353,44062,44514,73676,53103,63656,86911,77589,34976,58030,44753,57126,32946,46756,56955,49591,33545,57894,54075,46114,35188,6818,43768,30204,51853,67804,35710,50794,37350,77072,65795,72757,83421,61428,42097,19609,48979,37990,36194,13539,55040,64989,21483,47799,52387,65447,42521,46896,60383,43218,79163,73906,37596,49382,65252,67447,65209,59736,79281,47338,65950,38845,52676,40377,34478,56514,28947,42663,34723,43991,57194,23590,55351,71599,65064,58529,60229,46953,39884,38297,30124,43146,76594,58231,70391,25010,31386,50204,20414,51722,43628,55353,48586,51582,59325,61280,62970,50608,44688,47839,76778,49063,38877,49991,14157,34379,63316,62670,46878,12689,52446,54875,45691,23159,85480,48986,23370,50095,68191,73811,87717,26393,61817,45630,77554,39931,80442,41108,21452,51685,62385,33317,52141,56444,82181,46254,31561,27610,66868,61221,42678,52683,33431,40666,69713,66496,45605,25408,55648,47493,54908,48259,67704,51377,36512,49378,22940,62681,60543,60604,48169,54411,21308,90470,41590,39679,41258,75458,34611,46723,59795,50064,52374,30650,16956,49282,22840,46477,59569,59923,71358,74205,49976,58645,46651,17141,33190,59916,56914,83395,25048,15166,42780,40138,23547,43398,34764,40918,47760,80876,39443,73837,57908,52724,55108,75529,19736,47290,45880,85256,32339,55995,47343,26462,61661,70258,36090,62992,18005,65446,63900,68704],28443)) #6
# print(s.solve([1,2,3,4],1)) #6
# print(s.solve([1,2,3,4],2)) #6
print(s.solve([22,10,5,11,16,2,11,7,16,2,17,6,15,3,9,6],183)) #6