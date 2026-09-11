class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s += str(len(i)) + "#" + i
        return s


    def decode(self, s: str) -> List[str]:
        strs = []
        c = 0

        while c < len(s):
            i = c
            while s[i] != "#":
                i += 1
            strs.append(s[i + 1: i + int(s[c:i]) + 1])
            c = i + int(s[c:i]) + 1
        return strs
            



