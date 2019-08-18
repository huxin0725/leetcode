class Solution:
    def twoSum(self, nums, target):
        for i in range(0, len(nums)):
            key = target-nums[i]
            if key in nums and nums.index(key)!=i:
                return [i, nums.index(key)]
x =Solution()
print(x.twoSum([2,5,7,9],14))
