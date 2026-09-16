class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #most simple, get the product of all elements in the array
        #go through the array and for each index, change the value to the product divide by value


        #without division:

        #make another array, iterate through nums and add add the product to it except for current index
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref [0] = 1
        suff[-1] = 1

        for i in range(1,n):
            pref[i] = nums[i-1] * pref[i -1]
            
        for i in range(n-2, -1, -1):
            suff[i] = suff [i+1] * nums[i+1]

        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res
