# 整数反转
# 注意同时考虑输入和输出都在题目要求范围内

class Solution:
    def reverse(self, x: int) -> int:
        import math
        if x>pow(2,31)-1 or x<-pow(2,31):
            return 0
        else:
            flag = 1
            if x<0 :
                flag = -1
                x = -1 * x

            l = []
            a = int(x/10)
            l.append(x%10)
            while a>0:
                b = a%10
                l.append(b)
                a = int(a/10)
            result = 0
            for i in range(len(l)):
                result = result+math.pow(10,(len(l)-i-1))*l[i]
            result = int(result*flag)
            if result>pow(2,31)-1 or result<-pow(2,31):
                return 0
            else:
                return result
s = Solution()
print(s.reverse(x=-256))