class Solution:
    def smallestNumber(self, pattern: str) -> str:        
        n = len(pattern)
        string_arr = []
        result = []

        for i in range(1, n + 2):
            string_arr.append(i)
            if i == n + 1 or pattern[i - 1] == 'I':
                while string_arr:
                    result.append(str(string_arr.pop()))

        return ''.join(result)