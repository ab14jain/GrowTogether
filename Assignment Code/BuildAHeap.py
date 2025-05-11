class Solution:
    # @param A: list of integers
    # @return: a list representing the binary min heap
    def build_heap(self, A):
        # code here

        def heapify(heap, i):

            while ((2*i + 1) < n):
                l = 2*i + 1
                r = 2*i + 2
                x = min(heap[i], heap[l])
                if r < n:
                    x = min(x, heap[r])

                if heap[i] == x:
                    break
                elif heap[l] == x:
                    heap[i], heap[l] = heap[l], heap[i]
                    i = l
                else:
                    heap[i], heap[r] = heap[r], heap[i]
                    i = r
            
        n = len(A)
        heap = A[:]
        for i in range((n-2)//2,-1,-1):
            heapify(heap, i)

        return heap
                    
            # if id < 0:
            #     return

            # left_child = 2 * id + 1
            # right_child = 2 * id + 2

            # if right_child < n:
            #     if heap[id] > heap[left_child] and heap[id] > heap[right_child]:
            #         if heap[left_child] < heap[right_child]:
            #             heap[id], heap[left_child] = heap[left_child], heap[id]
            #         else:
            #             heap[id], heap[right_child] = heap[right_child], heap[id]
            #     else:
            #         if heap[left_child] < heap[right_child]:
            #             heap[id], heap[left_child] = heap[left_child], heap[id]
            #         else:
            #             heap[id], heap[right_child] = heap[right_child], heap[id]
            # else:
            #     if heap[id] > heap[left_child]:                    
            #         heap[id], heap[left_child] = heap[left_child], heap[id]

            # heapify(heap, id-1)    
    

s=Solution()
print(s.build_heap([5,13,-2,11,27,31,0,19]))