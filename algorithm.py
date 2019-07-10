# class Solution(object):
#     def rotate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         k = k%len(nums)
#         nums[:] = nums[-k:]+nums[:-k]
#         return nums
#
# num=[-1,-100,3,99]
# a = Solution()
# b = a.rotate(num, 2)
# print b

import time, datetime



