class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixSum = [1] * (len(nums) + 1)
        suffixSum = [1] * (len(nums) + 1)
        for i in range(len(nums)):
            prefixSum[i+1] = nums[i] * prefixSum[i]
            suffixSum[len(nums)-1-i] = nums[len(nums)-1-i] * suffixSum[len(nums)-i]
        for i in range(len(nums)):
            nums[i] = prefixSum[i] * suffixSum[i+1]
        return nums