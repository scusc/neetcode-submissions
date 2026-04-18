class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        # Step 1: find peak
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        peak = left

        # Step 2: search left (increasing)
        l, r = 0, peak
        while l <= r:
            mid = (l + r) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val < target:
                l = mid + 1
            else:
                r = mid - 1

        # Step 3: search right (decreasing)
        l, r = peak + 1, n - 1
        while l <= r:
            mid = (l + r) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val > target:
                l = mid + 1
            else:
                r = mid - 1

        return -1