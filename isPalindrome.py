import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        upper_str = s.lower()
        upper_str = re.sub("((?![A-Za-z0-9]).)", "", upper_str)
        rev_str = upper_str[::-1]
        if rev_str == upper_str:
            return True


print(Solution.isPalindrome("s", "ab_a"))
