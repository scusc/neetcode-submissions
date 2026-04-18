class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = 0
        left = right = 0 
        res = []

        while window < k:
            right += 1
            window += 1

        while right <= len(nums):
            curMax = max(nums[left : right])
            res.append(curMax)        
            left += 1
            right += 1
        return res
