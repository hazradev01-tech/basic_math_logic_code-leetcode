class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        duplicate = -1
        missing = -1

        # Phase 1: Mark visited numbers by negating values at their target indices
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                duplicate = abs(num)
            else:
                nums[index] = -nums[index]

        # Phase 2: Find the positive value index (corresponds to the missing number)
        for i in range(len(nums)):
            if nums[i] > 0:
                missing = i + 1
                break

        return [duplicate, missing]
        