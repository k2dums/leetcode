class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_s={x:s.count(x) for x in set(s)}
        map_t={x:t.count(x) for x in set(t)}
        
        if map_s==map_t:
            return True
