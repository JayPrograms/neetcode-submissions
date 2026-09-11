class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0
        for i in range(len(height)):
            
            for j in range(i + 1, len(height)):
                water = min(height[i], height[j])*(j-i)
                if water > maxWater:
                    maxWater = water
        return maxWater