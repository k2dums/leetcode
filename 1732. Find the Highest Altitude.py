class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxl=0
        lat=0
        for x in gain:
            lat=lat+x
            maxl=max(maxl,lat)
        return maxl
