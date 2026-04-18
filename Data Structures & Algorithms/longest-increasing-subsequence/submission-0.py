class Solution:    
    def lengthOfLIS(self, nums: List[int]) -> int:
        indices = []  # indices[i] = index of smallest tail of LIS of length i+1

        for i, num in enumerate(nums):
            left, right = 0, len(indices) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[indices[mid]] < num:
                    left = mid + 1
                else:
                    right = mid - 1

            if left == len(indices):
                indices.append(i)
            else:
                indices[left] = i

        return len(indices)