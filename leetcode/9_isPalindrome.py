# 可以直接将原来的数反转后 比较两个数是否相等

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif 0<=x<10:
            return True
        else:
            # a = x%10
            # b = int(x/10)
            # number = []
            # number.append(a)
            # while b>0:
            #     x = b
            #     a = x % 10
            #     b = int(x/10)
            #     number.append(a)
            # for i in range(int(len(number)/2)):
            #     if number[i]!=number[len(number)-i-1]:
            #         return False
            # return True
            # print(number)
            number = 0
            b = x
            while x>0:
                a = x%10
                number = number*10+a
                x = int(x/10)

            if b == number:
                return True
            else:
                return False
s = Solution()
print(s.isPalindrome(12321))