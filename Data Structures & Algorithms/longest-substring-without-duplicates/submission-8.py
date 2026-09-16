class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #use a set to track what has been seen
        seen = set()

        l =0
        res=0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            res = max(res, r-l +1)
        return res

            
        
                