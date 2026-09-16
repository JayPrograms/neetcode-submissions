class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        #sort the list, then go through the list
        nums.sort()
        #for each index, have 2 pointers to the right adn to the end of the list
        l, r = 0, 0
        for i, a in enumerate(nums):
            #if left most index is pos, the sum of all idexes to right will be >0 because sorted
            if a > 0:
                break

            # to skip duplicates, if -1, -1, ...
            if i > 0 and a == nums[i-1]:
                continue
        #move the left pointer if the sum of the 3 numbers is too small
            l, r = i+1, len(nums) -1

            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l +=1
                    r -= 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
        return res
            
        #move right pointer if the sum is too large

        #if we get a sum of 0, save the 3 numbers 

        #if the left and rigfht pointers overlap, move index forward


