class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #have a hashmap of {} key = number   value = freq
        tracker = {}

        freq = [[] for i in range(len(nums)+1)]

        #loop through the list and conut freq of all numbers
        for num in nums:
            if num in tracker:
                tracker[num] += 1
            else:
                tracker[num] = 1

        for num, cnt in tracker.items():
            freq[cnt].append(num)
            #cannot do = num because it will overwrite other values

        res = []

        for i in range(len(freq) -1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res


