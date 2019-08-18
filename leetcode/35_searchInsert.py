class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        elif target<nums[0]:
            return 0
        elif target>nums[-1]:
            return len(nums)
        else:
            for i in range(len(nums)-1):
                if target>nums[i] and target<nums[i+1]:
                    return i+1

s = Solution()
print(s.searchInsert([1,3,4,5],2))
