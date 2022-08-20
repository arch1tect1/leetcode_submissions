class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()
        l = 0
        
        for i in range(len(s)):
            if s[i] == ' ':
                l = 0
            else:
                l+=1
        return l