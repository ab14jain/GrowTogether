from sortedcontainers import SortedSet


class NumberContainers:
    def __init__(self):
        self.indexes = {}  
        self.num_indices = {}  

    def change(self, index: int, number: int) -> None:
        if index in self.indexes:
            old_num = self.indexes[index]
            self.num_indices[old_num].discard(index)
            if not self.num_indices[old_num]:
                del self.num_indices[old_num]  

        
        self.indexes[index] = number
        if number not in self.num_indices:
            self.num_indices[number] = SortedSet()
        self.num_indices[number].add(index)

    def find(self, number: int) -> int:
        if number not in self.num_indices:
            return -1  
        return self.num_indices[number][0]  