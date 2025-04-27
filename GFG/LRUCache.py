#https://www.geeksforgeeks.org/problems/lru-cache/1
from collections import deque


class LRUCache:
      
    #Constructor for initializing the cache capacity with the given value.  
    def __init__(self, cap):
        #code here
        self.capacity = cap
        self.order = deque()
        self.cache = {}     

        
    #Function to return value corresponding to the key.
    def get(self, key):
        #code here
        
        if key in self.cache:
            self.order.remove(key)
            self.order.appendleft(key)
            return self.cache[key]
        
        return -1


        
        
    #Function for storing key-value pair.   
    def put(self, key, value):
        #code here
        
        if key in self.cache:
            self.order.remove(key)
            self.order.appendleft(key)
            self.cache[key] = value
        else: 
            if len(self.order) >= self.capacity:
                lru_key = self.order.pop() 
                del self.cache[lru_key]                 
                              
            self.order.appendleft(key)
            self.cache[key] = value      


cache = LRUCache(2)
cache.put(1,1)
cache.put(2,2)
print(cache.get(1))
cache.put(3,3)
print(cache.get(2))
cache.put(4,4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))