class Solution:
    # @param {int[]} nums1 an integer array of length m with digits 0-9
    # @param {int[]} nums2 an integer array of length n with digits 0-9
    # @param {int} k an integer and k <= m + n
    # @return {int[]} an integer array
    def maxNumber(self, nums1, nums2, k):
        # Write your code here
        len1, len2 = len(nums1), len(nums2)
        res = []
        for x in range(max(0, k - len2), min(k, len1) + 1):
            tmp = self.merge(self.getMax(nums1, x), self.getMax(nums2, k - x))
            res = max(tmp, res)
        return res

    def getMax(self, nums, t):
        ans = []
        size = len(nums)
        for x in range(size):
            while ans and len(ans) + size - x > t and ans[-1] < nums[x]:
                ans.pop()
            if len(ans) < t:
                ans.append(nums[x])
        return ans

    def merge(self, nums1, nums2):
        return [max(nums1, nums2).pop(0) for _ in nums1 + nums2]
s = Solution()
num1 = [3, 4, 6, 5]
num2 = [5, 3, 2, 5, 8, 3]
print s.maxNumber(num1,num2,8)