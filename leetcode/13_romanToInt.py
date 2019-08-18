class Solution:
    def romanToInt(self, s: str) -> int:
        def number(a):
            if a=='I':
                return 1
            elif a=='V':
                return 5
            elif a=='X':
                return 10
            elif a=='L':
                return 50
            elif a=='C':
                return 100
            elif a=='D':
                return 500
            elif a=='M':
                return 1000
        result = 0
        if len(s)==1:
            return number(s)
        else:
            for i in range(len(s)-1):
              key = number(s[i])
              key1 = number(s[i+1])
              if key<key1:
                  result=result-key
              else:
                  result=result+key
            result= result+key1

            return result

s = Solution()
print(s.romanToInt('VI'))