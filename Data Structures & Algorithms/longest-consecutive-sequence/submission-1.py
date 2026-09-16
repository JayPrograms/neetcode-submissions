class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #sort the array then have a counter as you traverse left to right and count the sequence


        #without sorting:

        #add it all to a set

        #traverse through the set, if the prev number doesnt exist, this is the start of the sequence

        #check if the next number exists, and incremeant a counter if it does

        #if the next number doesnt exist, this is the end of the list

        numset = set(nums)
        length = 0
        longest = 0

        for num in numset:
            if (num-1) not in numset:
                length = 1

                while (num+length) in numset:
                    length +=1
                longest = max(longest, length)
        
        return longest
            

