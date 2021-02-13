import math
class Solution:
    def numberOfMatches(self, n: int) -> int:
        
        if n==1:
            return 0
        
        matches=0
        while(n>1):
            value=n/2.0
            n=math.ceil(value)
            matches=matches+math.floor(value)
        return matches
