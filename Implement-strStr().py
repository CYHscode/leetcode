class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l1 = len(haystack)
        l2 = len(needle)
        if l2 == 0:
            return 0
        for i in range(l1-l2+1):
            if haystack[i:i+l2] == needle[:]:  #needle代入1字符串
                return i
        return -1
