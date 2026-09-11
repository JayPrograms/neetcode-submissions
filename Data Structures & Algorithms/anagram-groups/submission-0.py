class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortMap = {}

        for i in range(len(strs)):
            if ''.join(sorted(strs[i])) in sortMap:
                sortMap[''.join(sorted(strs[i]))].append(strs[i])
            else:
                sortMap[''.join(sorted(strs[i]))] = [strs[i]]
        return list(sortMap.values())    
