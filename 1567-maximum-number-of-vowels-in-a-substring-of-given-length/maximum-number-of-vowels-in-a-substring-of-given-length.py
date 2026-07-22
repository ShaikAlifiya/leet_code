class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=set('aeiou')
        c=0
      
        for i in range(k):
            if s[i] in vowels:
                 c+=1
            ms=c     
        for i in range(k,len(s)):
            if s[i] in vowels:
                c+=1
            if s[i-k] in vowels:
                c-=1
            ms=max(ms,c) 
        return ms       

        