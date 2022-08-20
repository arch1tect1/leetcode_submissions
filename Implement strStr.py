class Solution(object):
    def strStr(self, haystack, needle):
        if haystack is None or needle is None:
            return -1
        if haystack == needle:
            return 0
        needleLength = len(needle)
        for i in range(len(haystack) - needleLength + 1):
            if haystack[i:i + needleLength] == needle:
                return i
        return -1