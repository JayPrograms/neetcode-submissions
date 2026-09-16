class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #split t into a hashmap. 
        charcount, windows = {}, {}
        for char in t:
            charcount[char] = 1+ charcount.get(char, 0)

        #make a window, expand and add characters to a hashmap. each time compare if the hashmap for t is a subset of hashmap of s. once it is, move left pointer right until t is no longer subset of s then return the previous window.

        if t == "":
            return ""

        #how many chars meet the count
        have = 0
        #how many characters we need t omatch
        need = len(charcount)

        res = [-1, -1]
        reslen = float("infinity")

        l = 0

        for r in range(len(s)):
            c = s[r]
            #make the hashmap of the characters in s
            windows[c] = 1 + windows.get(c, 0)

            #check how many characters match in both hashmaps for s and t
            if c in charcount and windows[c] == charcount[c]:
                have += 1
            
            #if our window over s has all the characters required from t, move the left pointer to the right to close down the window as long as the condition stays ture
            while have == need:

                #update the length of the window to the the smaller size
                if(r - l + 1) < reslen:
                    res = [l, r]
                    reslen = r - l + 1

                    #move pointer to right, so decremeant the char that was removed from the hashmap
                windows[s[l]] -= 1
                if s[l] in charcount and windows[s[l]] < charcount[s[l]]:
                    have -= 1
                l += 1
        l,r =  res
        return s[l : r + 1] if reslen != float("infinity") else ""



        