class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            index = int((left + right)/2)
            if nums[index] == target:
                return index
            elif nums[index] > target:
                right = index 
            else:
                left = index + 1

        return -1