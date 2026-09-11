class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #have a dictionary
        dict1 = {}

        for i in range(len(s)):
            if s[i] in dict1:
                dict1[s[i]] += 1
            
            else:
                dict1[s[i]] = 1
        
        for char in t:
            if char not in dict1:
                return False
            
            dict1[char] -= 1

            if dict1[char] == 0:
                del dict1[char]
        

        if dict1:
            return False

        return True
