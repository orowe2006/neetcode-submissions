class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        keeper = {}

        for i in range(len(nums)):
            if nums[i] not in keeper:
                keeper[nums[i]] = 0
            keeper[nums[i]] += 1

        keeper = sorted(keeper.items(), key=lambda x: x[1], reverse=True)

        l = []

        for i in range(k):
            l.append(keeper[i][0])

        return l