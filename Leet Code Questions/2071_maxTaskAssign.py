import bisect
from typing import List


class Solution:
    
    def can_assign(self, mid, workers, tasks, pills, strength):
        usable_workers = sorted(workers[-mid:])
        for i in range(mid - 1, -1, -1):
            task = tasks[i]
            if usable_workers[-1] >= task:
                usable_workers.pop()
            else:
                if pills <= 0:
                    return False
                # Find the weakest worker who can do the task with pill
                idx = bisect.bisect_left(usable_workers, task - strength)
                if idx == len(usable_workers):
                    return False
                pills -= 1
                usable_workers.pop(idx)
        return True
    
    def maxTaskAssign(self, tasks, workers, pills, strength):
        tasks.sort()
        workers.sort()
        low, high = 0, min(len(tasks), len(workers))
        assigned = 0
        
        while low <= high:
            mid = low + (high - low) // 2
            if self.can_assign(mid, workers, tasks, pills, strength):
                assigned = mid
                low = mid + 1
            else:
                high = mid - 1
        return assigned
    
    #def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        
        

        # tasks.sort()
        # workers.sort()
          
        # count = 0

        # i = 0
        # j = 0

        # completed_tasks = []
        # used_worker = []
        # left_tasks = []
        # left_worker = []

        # while i < len(workers):

        #     if workers[i] >= tasks[j]:
        #         completed_tasks.append(tasks[j])
        #         used_worker.append(workers[i])
        #         count += 1
        #         j += 1
        #     else:                
        #         left_worker.append(workers[i])

        #     i += 1
        
        # for t in tasks:
        #     if t not in completed_tasks:
        #         left_tasks.append(t)

        # i = 0
        # j = 0

        # while i < len(left_worker):

        #     if left_worker[i] >= left_tasks[j]:

        #         count += 1

        #         i += 1
        #         j += 1
        #     else:
        #         if pills :
        #             if (left_worker[i]+strength) >= left_tasks[j]:

        #                 count += 1

        #                 i += 1
        #                 j += 1

        #                 pills -= 1
        #             else:
        #                 i += 1
        #         else:
        #             i += 1

        # return count
    
s=Solution()
# print(s.maxTaskAssign([5,9,8,5,9], [1,6,4,2,6], 1, 5))
print(s.maxTaskAssign(tasks = [3,2,1], workers = [0,3,3], pills = 1, strength = 1))
# print(s.maxTaskAssign(tasks = [5,4], workers = [0,0,0], pills = 1, strength = 5))
# print(s.maxTaskAssign(tasks = [10,15,30], workers = [0,10,10,10,10], pills = 3, strength = 10))
                


