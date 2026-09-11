class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #have a dictionary
        dict1 = {}
        dict2 = {}

        for i in range(len(s)):
            if s[i] in dict1:
                dict1[s[i]] += 1
            
            else:
                dict1[s[i]] = 1
        
        for i in range(len(t)):
            if t[i] in dict2:
                dict2[t[i]] += 1
            
            else:
                dict2[t[i]] = 1
        
        print(dict1, dict2) 

        if dict1 == dict2:
            return True

        
        
        return False
