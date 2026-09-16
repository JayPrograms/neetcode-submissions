class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            #base case, the total is equal to target, so save it to the res array
            if total == target:
                res.append(cur.copy())
                return

            #if we use all the diff numbers we are given, or if the total goes over the target, stop
            if i >= len(nums) or total > target:
                return          

            cur.append(nums[i])
            dfs(i, cur, total+nums[i])
            cur.pop()
            dfs(i+1, cur, total)

        dfs(0, [], 0)

        return res

