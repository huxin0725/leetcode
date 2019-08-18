class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        result = ''
        num = 0
        if len(strs)==0:
            return result
        elif len(strs)==1:
            return strs[0]
        while(1):
            for i in range(1, len(strs)):
                if num >= len(strs[0]) or num >= len(strs[i]):
                    return result
                elif strs[0][num] != strs[i][num]:
                    return result
            result=result+strs[0][num]
            num = num+1


s = Solution()
print(s.longestCommonPrefix([]))