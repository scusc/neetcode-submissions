class Solution:
    def isPotentialCandidateToSplit(self, mid, nums, k):
        subArraysCount = 0
        curSum = 0
        for num in nums:
            curSum += num
            if curSum > mid:
                subArraysCount += 1
                curSum = num
        return subArraysCount + 1 <= k 

    def splitArray(self, nums: List[int], k: int) -> int:
        leftbound, rightbound = max(nums), sum(nums)
        res = rightbound

        while leftbound <= rightbound:
            mid = leftbound + ((rightbound - leftbound) // 2)
            if self.isPotentialCandidateToSplit(mid, nums, k):
                res = mid
                rightbound = mid - 1
            else:
                leftbound = mid + 1
        
        return res