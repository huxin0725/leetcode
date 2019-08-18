# 使用split分割 然后考虑多个空格的情况

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.split(' ')
        if len(a)==1:
            return len(a[0])
        if len(a[-1])==0:
            i = -1
            while i>=-len(a):
                if len(a[i])!=0:
                    return len(a[i])
                i=i-1
            return 0
        else:
            return len(a[-1])

s = Solution()
print(s.lengthOfLastWord("b   a    "))