class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count=0
        for attr in items:
            if (ruleKey =="type" and ruleValue==attr[0]) or (ruleKey=="color" and ruleValue==attr[1]) or (ruleKey=="name" and ruleValue==attr[2]):
                count+=1
        return count
                
        
