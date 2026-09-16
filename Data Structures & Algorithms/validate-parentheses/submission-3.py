class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        hm = {")" : "(", "]" : "[", "}" : "{" } #key = closing bracket  value = opening bracket

        for char in s:
            if char in hm:
                if stack and stack[-1] == hm[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)


        if stack:
            return False
        return True
            
            