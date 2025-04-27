import heapq
from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        
        # seats.sort()
        # students.sort()
        # res = 0
        # for i in range(len(seats)):
        #     res += abs(seats[i]-students[i])

        # return res

        min_heap_seats = []
        min_heap_students = []

        res = 0

        for i in range(len(seats)):
            heapq.heappush(min_heap_seats, seats[i])
            heapq.heappush(min_heap_students, students[i])       
            

        while min_heap_seats:

            seat = heapq.heappop(min_heap_seats)
            std = heapq.heappop(min_heap_students)

            res += abs(seat-std)

        return res
