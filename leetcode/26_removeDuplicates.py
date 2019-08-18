# 把重复的替换

class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        top = 0
        for i in range(len(nums)):
            if nums.index(nums[i])>=top:
                #a = nums[top]
                nums[top] = nums[i]
                #nums[i] = a
                top = top+1
        return top

s = Solution()
print(s.removeDuplicates([1,1,2,2,3,4]))