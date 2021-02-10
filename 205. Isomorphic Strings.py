class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if(len(s)!= len(t)):
            return False
        
        unique_s=list(dict.fromkeys(s))
        unique_t=list(dict.fromkeys(t))
        if (len(unique_s)!= len(unique_t)):
            return False
        
        mapping={x:y for x,y in zip(unique_s,unique_t)}
        for x,y in zip(s,t):
            if mapping[x]!=y:
                return False
        return True
        
