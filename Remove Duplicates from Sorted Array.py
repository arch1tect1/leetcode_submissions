class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        else: 
            m = 0
            i = 1
            while i < len(nums) - m:
                if nums[i] == nums[i-1]:
                    n = nums.pop(i)
                    nums.append(n)
                    m += 1
                else:
                    i += 1
            return len(nums) - m