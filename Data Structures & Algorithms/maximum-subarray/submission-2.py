class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        sums = lowest = nums[0]
        print(nums)
        for i in range(1, len(nums)):
            num = nums[i]
            sums = max(sums, num - lowest, num)
            lowest = min(lowest, num)
        return sums