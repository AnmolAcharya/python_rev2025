class Solution:
    def romanToInt(self, s: str) -> int:

        


hash_map = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D': 500, 'M':1000}
        sum = 0
        i =0

        while i < len(s):
            if i < len(s) - 1 and hash_map[s[i]] < hash_map[s[i+1]]:
                diff = hash_map[s[i+1]] - hash_map[s[i]]
                sum += diff 
                i += 2
            else:
                sum += hash_map[s[i]]
                i += 1
                
        return sum



















        