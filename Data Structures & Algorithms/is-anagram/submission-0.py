class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #count how many of each characters are in string
        hashmapS = {}
        hashmapT = {}

        for i in range(len(s)):
            if s[i] in hashmapS:
                hashmapS[s[i]] = hashmapS[s[i]] + 1
            else:
                hashmapS[s[i]] = 1

        for i in range(len(t)):
            if t[i] in hashmapT:
                hashmapT[t[i]] = hashmapT[t[i]] + 1
            else: 
                hashmapT[t[i]] = 1
        if hashmapT == hashmapS:
            return True
        return False