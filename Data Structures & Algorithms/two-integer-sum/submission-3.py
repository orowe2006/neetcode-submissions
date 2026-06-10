class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # iterate over nums, you know what number is necessary to find
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums:
                j = nums.index(complement)
                if j != i:
                    return sorted([i, j])