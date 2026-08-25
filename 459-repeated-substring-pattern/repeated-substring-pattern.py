class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        pattern=1
        for i in range(1,len(s)):
            if (len(s)%i==0):
                pattern=s[:i]
                pattern=pattern*(len(s)//i)
                if pattern==s:
                    return True
        return False                    