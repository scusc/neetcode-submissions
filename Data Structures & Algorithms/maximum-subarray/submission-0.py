class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp = nums[0]
        maxi = nums[0]

        for num in nums[1:]:
            temp = max(num, temp + num)
            maxi = max(maxi, temp)
        
        return maxi
        