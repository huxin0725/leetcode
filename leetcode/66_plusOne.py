class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        flag = 1
        for i in range(len(digits)):
            j = len(digits)-1-i
            a = digits[j]+flag
            flag = int(a/10)
            digits[j] = int(a%10)

            if flag == 0:
                break
        if flag == 1:
            digits.insert(0,1)
        return digits

s = Solution()
print(s.plusOne([9,9,9]))