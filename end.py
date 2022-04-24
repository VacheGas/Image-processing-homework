class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        if not len(s):
            return s
        j = len(s) - 1
        for i in range(0, len(s) // 2):
            s[i], s[j] = s[j], s[i]
            j -= 1
        return s