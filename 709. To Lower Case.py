class Solution:
    def toLowerCase(self, str: str) -> str:
        ans=""
        for i in str:
            if ord(i)>=97 and ord(i)<=122 or not(ord(i)>=65 and ord(i)<=90):
                ans=ans+i
            else:
                ans=ans+ chr(ord(i)+32)
             
        return ans
