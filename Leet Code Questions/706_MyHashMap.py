class MyHashMap:


    def __init__(self):
        self.hashmap = {}
        

    def put(self, key: int, value: int) -> None:
        self.hashmap[key] = value
        

    def get(self, key: int) -> int:
        return self.hashmap.get(key, -1)
        

    def remove(self, key: int) -> None:

        if key in self.hashmap:
            self.hashmap.pop(key)
        return
        


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
key = 1
value = 2
obj.put(key,value)
param_2 = obj.get(key)
print(param_2)
obj.remove(key)
param_2 = obj.get(key)
print(param_2)