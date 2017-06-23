class TrappingRainWater(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        length = len(height)
        left = 0
        right = length - 1
        sec_high = 0
        area = 0
        while left < right:
            if height[left] < height[right]:
                sec_high = max(sec_high, height[left])
                area += sec_high - height[left]
                left += 1
            else:
                sec_high = max(sec_high, height[right])
                area += sec_high - height[right]
                right -= 1
        return area


if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    tr = TrappingRainWater()
    area = tr.trap(height)
    print area
