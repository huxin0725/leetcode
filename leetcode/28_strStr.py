# 字符串find子串 找到返回起始位置 找不到返回-1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == None:
            return 0
        else:
            return haystack.find(needle)

s = Solution()
print(s.strStr('hello','a'))