class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        num = 0
        i = 0
        a = []
        while i < len(s):
            a.append(s[i])
            j = i+1
            while j < len(s) and s[j] not in a:
                a.append(s[j])
                j=j+1
            num = max(num, len(a))
            if j< len(s):
                idx = a.index(s[j])
                a = a[idx+1:]
            i = j

        return num

s = Solution()
print(s.lengthOfLongestSubstring("dvdf"))