class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        max = 0

        nums.sort()

        print(nums)

        for i in range(len(nums)-1):

            if nums[i+1] == nums[i]:
                continue

            if nums[i+1] - nums[i] == 1:
                count+=1
            else:
                count = 0

            if max < count:
                max = count

        return max + 1 if len(nums) > 0 else 0