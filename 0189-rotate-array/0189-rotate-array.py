class Solution(object):

  def rotate(self, nums, k):
    n = len(nums)
    k %= n  # Handles cases where k > n
    nums[:] = nums[n - k :] + nums[: n - k]
      
        