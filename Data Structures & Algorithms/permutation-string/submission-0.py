class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1_freq = [0]*26
        for c in s1:
            s1_freq[ord(c)-ord('a')]+=1
        l = 0
        s2_freq = [0]*26
        for r in range(len(s2)):
            if (r-l+1) > len(s1):
                s2_freq[ord(s2[l])-ord('a')]-=1
                l+=1
            s2_freq[ord(s2[r])-ord('a')]+=1
            if s2_freq == s1_freq:
                return True
        return False

