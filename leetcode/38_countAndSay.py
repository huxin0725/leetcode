class Solution:
    def countAndSay(self, n: int) -> str:
        def trans(s):
            a = ''
            count = 1
            b = '1'
            for i in range(1,len(s)):

                b = s[i-1]
                if s[i]==s[i-1]:
                    count+=1
                else:
                    a = a+str(count)+b
                    count = 1
                    b = s[i]
            a = a+str(count)+b

            return a

        result = '1'
        if n == 1:
            return result
        for i in range(1,n):
            result=trans(result)

        return result

s = Solution()
print(s.countAndSay(5))