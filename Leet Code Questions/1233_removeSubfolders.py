class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        seen = set()
        folder.sort()  
        for f in folder:            
            temp_folder = f[:]   
            rightIndex = f.rfind("/")
            f = f[:rightIndex]     
            while f != "":
                if f in seen:
                    break
                f = f[:rightIndex]
            else:
                seen.add(temp_folder)           
            

        return list(seen)


# Time complexity: O(n)
# Space complexity: O(n)
# where n is the length of the input list folder
# and m is the length of the longest string in folder
# and k is the number of strings in folder
# and l is the number of unique strings in folder
# and p is the number of unique strings in seen
#   

s = Solution()

print(s.removeSubfolders(["leetcode"])) # ["/a","/c/d","/c/f"]  
print(s.removeSubfolders(["/leetcode/problems","/leetcode"])) # ["/a","/c/d","/c/f"]  
print(s.removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"])) # ["/a","/c/d","/c/f"]  
print(s.removeSubfolders(["/a","/a/b/c","/a/b/d"])) # ["/a"]
print(s.removeSubfolders(["/a/b/c","/a/b/ca","/a/b/d"])) # ["/a/b/c","/a/b/ca","/a/b/d"]

