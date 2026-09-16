class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #have a hashmap of {} key = number   value = freq
        tracker = {}

        #loop through the list and conut freq of all numbers
        for num in nums:
            if num in tracker:
                tracker[num] += 1
            else:
                tracker[num] = 1


        #return keys that has the max value. maybe use a min heap
        heap = []
        for num in tracker.keys():
            heapq.heappush(heap, (tracker[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res