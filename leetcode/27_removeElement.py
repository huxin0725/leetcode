class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        if val not in nums:
            return len(nums)
        a = len(nums)-1
        while nums.index(val)<=a and a>=0:
            nums[nums.index(val)] = nums[a]
            nums[a] = val
            a=a-1
        return a+1

s = Solution()
print(s.removeElement([1,1,2,2,3,4],2))