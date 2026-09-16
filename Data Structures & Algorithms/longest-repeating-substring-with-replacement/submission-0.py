class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #have a window with the rules:
        #move right pointer when it is the same character
        #move rp if diff character but less than k diff characers have appeared
        #window size - count of most freq chars <= k


        count = {}
        res = 0

        l = 0
        maxf = 0

        for r in range(len(s)):
            #increase the freq of the character that we are processing
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            #move the left pointer if the # of not most freq characerts is more than K
            while (r-l+1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l +1)

        return res
