class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        s_nums=nums.copy()
        s_nums=list(dict.fromkeys(nums))
        s_nums.sort()
        
        i=s_nums[0]
        start=s_nums[0]
        maxl=1
        
        for element in s_nums:
            
            if i != element:
                maxl=max(maxl,i-start)
                start=element
                i=element
            i+=1
        maxl=max(maxl,s_nums[-1]-start+1)
        return maxl
                
        
