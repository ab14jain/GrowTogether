from collections import defaultdict, deque
from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        

        # adj = defaultdict(list)

        # for i in range(len(ingredients)):
        #     adj[recipes[i]].append(ingredients[i])

        # ans = []
        # x = 0
        # for indg in ingredients:
        #     hasAllIngredients = True
        #     recipe = recipes[x]

        #     for i in indg:           
        #         if i not in supplies:
        #             hasAllIngredients = False
        #             break

        #     finalIndg = []
        #     hasAllIngredients = True
        #     for y in indg:
        #         if y in adj:
        #             for z in adj[y]:
        #                 finalIndg.extend(z)
        #         else:
        #             finalIndg.append(y)

        #     for i in finalIndg:           
        #         if i not in supplies:
        #             hasAllIngredients = False
        #             break
            
        #     if hasAllIngredients:
        #         ans.append(recipe)
            
        #     x += 1
        
        # return ans            

        adj = defaultdict(list)
        indegree = {}
        supply = set(supplies)
        
        for i in range(len(recipes)):
            recipe = recipes[i]
            indegree[recipe] = 0
            for ingredient in ingredients[i]:
                if ingredient not in supply:
                    adj[ingredient].append(recipe)
                    indegree[recipe] += 1

        q = deque()
        for recipe, deg in indegree.items():
            if deg == 0:
                q.append(recipe)

        
        res = []
        while q:
            curr_recipe = q.popleft()
            res.append(curr_recipe)

            for next_recipe in adj.get(curr_recipe, []):
                indegree[next_recipe] -= 1
                if indegree[next_recipe] == 0:
                    q.append(next_recipe)

        return res



s=Solution()
print(s.findAllRecipes(recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]))
print(s.findAllRecipes(recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]))
print(s.findAllRecipes(recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]))