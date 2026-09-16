class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        #for each word in the list
        for s in strs:
            #create an empty array that we will use to count the freq of each letter in the word
            count = [0] * 26

            for c in s:
                #add freq of each letter into the count array
                count[ord(c) - ord('a')] += 1
            #add the frequencies to the hashmap as the key and the word as the value
            result[tuple(count)].append(s)
            #return the hashmap values as a list
        return list(result.values())