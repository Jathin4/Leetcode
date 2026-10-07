class Solution:
    def maxArea(self, height: list[int]) -> int:
        mw = 0
        l = 0
        r = len(height)-1
        while l < r:
            w = r-l
            ch = min(height[l],height[r])
            cw = w*ch
            mw = max(mw,cw)
            if height[l]< height[r]:
                l += 1
            else:
                r -= 1
        return mw