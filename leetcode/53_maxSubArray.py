class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        if len(nums)==1:
            return nums[0]

        a = nums[0]
        tmp = a
        for i in range(1,len(nums)):
            if a+nums[i]>nums[i]:
                tmp = max(tmp,a+nums[i])
                a = a+nums[i]
            else:
                tmp = max(tmp, a+nums[i],a,nums[i])
                a = nums[i]

        return tmp



s = Solution()
print(s.maxSubArray([1,2,-1,-2,2,1,-2,1,4,-5,4]))