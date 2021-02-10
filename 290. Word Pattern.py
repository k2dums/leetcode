class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split(" ")
        pats=list(pattern) #Returns a list of characters of that list
        unique_words=list(dict.fromkeys(words))
        unique_pats=list(dict.fromkeys(pats))
        if (len(words)!=len(pats)) or (len(unique_pats)!=len(unique_words)):
            return False
        mapping={x:y for (x,y) in zip(unique_words,unique_pats)}
        flag=True
        for word,pat in zip(words,pats):
            if mapping[word]!=pat:
                flag=False
                break
        return flag
        
