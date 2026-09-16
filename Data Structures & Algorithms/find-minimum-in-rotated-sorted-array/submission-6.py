class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        

        res = nums[0]

        while l <= r:
            #unrotated
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            mid = l+r
            mid = mid//2

            res = min(res, nums[mid])

            if nums[mid] >= nums[l]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid - 1

        
        return res
            

        

        