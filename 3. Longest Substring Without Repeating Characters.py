class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1  
        if len(s)==2 and s[0]!=s[1]:
            return 2
        if len(set(s))==1:
            return 1
        
        start=0
        length=1
        maxl=0
        for i in range(1,len(s)):
            #checking if the character is not in substring
            if s[i] not in s[start:i]:
                length+=1
            #if the character is in the substring
            else:
                maxl=max(maxl,length)
                if s[i]==s[i-1]:
                    length=1
                    start=i
                else:
                    start=s.index(s[i],start,i)+1
                    length=i-start+1
                
        
                      
        maxl=max(maxl,length)
        return maxl
                
                
