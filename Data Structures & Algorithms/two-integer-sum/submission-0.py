class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}

        for i in range(len(nums)):
            if (target - nums[i]) not in hashset:
                hashset[nums[i]] = i
            else:
                return [hashset[(target - nums[i])], i]