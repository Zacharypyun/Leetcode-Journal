class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h = {}
        x = {}
        for i in s:
            if i in h:
                h[i]+=1
            else:
                h[i] = 1
        for i in t:
            if i in x:
                x[i]+= 1
            else:
                x[i] = 1
        return x == h
        
