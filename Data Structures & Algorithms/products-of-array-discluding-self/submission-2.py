class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        count = 0

        for n in nums:
            if count == 0 and n == 0:
                count = 1
            elif count == 1 and n == 0:
                product = 0
                break
            else:
                product *= n

        for i in range(len(nums)):
            if nums[i] != 0 and count == 1:
                nums[i] = 0
            elif nums[i] != 0:
                nums[i] = (int)(product / nums[i])
            else:
                nums[i] = product
            

        return nums