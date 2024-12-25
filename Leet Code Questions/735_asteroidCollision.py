class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:

        stack = []
        n = len(asteroids)
        for i in range(n):
            curr_asteroids = asteroids[i]
            if curr_asteroids > 0:
                stack.append(curr_asteroids)
            else:
                if len(stack) == 0 or stack[-1] < 0:
                    stack.append(curr_asteroids)
                else:
                    while stack and stack[-1] > 0:
                        if abs(stack[-1]) == abs(curr_asteroids):
                            stack.pop()
                            curr_asteroids = 0
                        elif stack[-1] < abs(curr_asteroids):
                            stack.pop()                            
                        else:
                            break

                        
                    if len(stack) == 0 or stack[-1] < 0:
                        if curr_asteroids != 0:
                            stack.append(curr_asteroids)
                    if len(stack) == 0 and curr_asteroids != 0:
                        stack.append(curr_asteroids)

        return stack

s= Solution()
print(s.asteroidCollision([-5,-4,-3,-2,1,-6,-5,-3])) # [5, 10]
print(s.asteroidCollision([5,4,3,2,1,-6])) # [-6]
print(s.asteroidCollision([5, 10, -5])) # [5, 10]
print(s.asteroidCollision([8, -8])) # []
print(s.asteroidCollision([10, 2, -5])) # [10]
print(s.asteroidCollision([-2, -1, 1, 2])) # [-2, -1, 1, 2]