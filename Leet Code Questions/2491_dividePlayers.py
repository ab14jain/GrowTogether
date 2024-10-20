class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        skill.sort()
        product_sum = 0

        x = 0
        y = len(skill) - 1        
        skill_sum = skill[x] + skill[y]
        while x < y: 
            x += 1
            y -= 1
            if skill_sum != skill[x] + skill[y]:
                return -1

        
        i = 0
        j = len(skill) - 1
        
        while i < j:            
            product_sum += skill[i] * skill[j]
            i += 1
            j -= 1
        
        return product_sum
        
    

test = Solution()

print(test.dividePlayers([3,2,5,1,3,4])) # 22
print(test.dividePlayers([3,4])) # 12
print(test.dividePlayers([1,1,2,3])) # -1
        