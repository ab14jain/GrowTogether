class ProductOfNumbers:

    def __init__(self):
        self.pref_prod = [1]
        self.last_zero_idx = -1
        

    def add(self, num: int) -> None:
        pref = self.pref_prod[-1]
        if pref != 0:            
            self.pref_prod.append(pref*num)            
        else:
            self.pref_prod.append(num)
        
        if num == 0:
            self.last_zero_idx = len(self.pref_prod) - 1
        

    def getProduct(self, k: int) -> int:
        n = len(self.pref_prod)
        all_p = self.pref_prod[n-1]
        divi = self.pref_prod[n-k-1]

        
        if self.last_zero_idx >= n-k:
            return 0
        elif divi == 0:
            return all_p
        else:
            return all_p // divi

        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

obj = ProductOfNumbers()
obj.add(3)
obj.add(0)
obj.add(2)
obj.add(5)
obj.add(4)
param_2 = obj.getProduct(2)
print(param_2)
param_2 = obj.getProduct(3)
print(param_2)
param_2 = obj.getProduct(4)
print(param_2)
obj.add(8)
param_2 = obj.getProduct(2)
print(param_2)