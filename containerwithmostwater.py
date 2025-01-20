class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height)-1 # two pointers
        distance = 0
        # twosum like strategy
        while l < r: # Iterate through the array
            distance = max(distance, min(height[l], height[r]) * (r - l))
            # We want to keep the lines with taller height 
            # because taller height can give a better max area.
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return distance